import os
import xml.etree.cElementTree as ET
from shutil import copyfile

import yaml
from PIL import Image
from plumbum import local
from plumbum.cmd import sh, zip, unzip, rm


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.abspath(
    os.path.join(
        SCRIPT_DIR,
        '../data/raw/bosch/',
    )
)
TEMP_DIR = os.path.join(DATASET_DIR, 'temp')
TARGET_DIR = os.path.abspath(
    os.path.join(
        SCRIPT_DIR,
        '../data/bosch',
    )
)


def run():
    with local.cwd(DATASET_DIR):
        sh('-c', 'cat dataset_train_rgb.zip.* > dataset_train_rgb.zip')
        zip['-FF', 'dataset_train_rgb.zip', '--out', 'dataset_train_rgb_fixed.zip']()
        unzip['dataset_train_rgb_fixed.zip', '-d', TEMP_DIR]()
        rm['dataset_train_rgb_fixed.zip']['dataset_train_rgb.zip']()

    annotations_dir = os.path.join(TARGET_DIR, 'annotations')
    if not os.path.exists(annotations_dir):
        os.makedirs(annotations_dir)

    image_destination_dir = os.path.join(TARGET_DIR, 'images')

    with open(os.path.join(TEMP_DIR, 'train.yaml'), 'r') as stream:
        anootation_data = yaml.load(stream)

    for index, datum in enumerate(anootation_data):
        xml_root = ET.Element("annotation")

        ET.SubElement(xml_root, "folder").text = 'bosch'
        ET.SubElement(xml_root, "filename").text = datum['path']

        size = ET.SubElement(xml_root, "size")
        ET.SubElement(size, "width").text = '1280'
        ET.SubElement(size, "height").text = '720'
        ET.SubElement(size, "depth").text = '3'

        for bbox in datum['boxes']:
            box_label = bbox['label'].lower().strip()
            if box_label in [
                'redleft', 'redright', 'redstraight', 'redstraightleft',
            ]:
                box_label = 'red'
            elif box_label in [
                'greenleft', 'greenright', 'greenstraight',
                'greenstraightright', 'greenstraightleft',
            ]:
                box_label = 'green'

            obj = ET.SubElement(xml_root, "object")
            ET.SubElement(obj, "name").text = box_label

            bndbox = ET.SubElement(obj, "bndbox")
            ET.SubElement(bndbox, "xmin").text = str(bbox['x_min'])
            ET.SubElement(bndbox, "ymin").text = str(bbox['y_min'])
            ET.SubElement(bndbox, "xmax").text = str(bbox['x_max'])
            ET.SubElement(bndbox, "ymax").text = str(bbox['y_max'])

        output_filepath = os.path.join(annotations_dir, '{:06d}.xml'.format(index + 1))
        tree = ET.ElementTree(xml_root)
        tree.write(output_filepath)

        # copy image (and convert to jpg, if needed)
        source_path = os.path.join(TEMP_DIR, datum['path'])
        destination_path = os.path.join(image_destination_dir, datum['path'])
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))
        copyfile(
            source_path,
            destination_path,
        )


if __name__ == '__main__':
    run()
