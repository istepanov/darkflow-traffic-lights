import os
import xml.etree.cElementTree as ET

import yaml


def convert_annotations(input_filename, target_path):
    input_filename = 'data/bosch_traffic_lights/train.yaml'
    target_path = 'data/bosch_dataset/annotations'

    with open(input_filename, 'r') as stream:
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
            
        tree = ET.ElementTree(xml_root)

        output_filepath = os.path.join(
            target_path,
            '{:06d}.xml'.format(index + 1)
        )

        tree.write(output_filepath)


if __name__ == '__main__':
    convert_annotations(None, None)
