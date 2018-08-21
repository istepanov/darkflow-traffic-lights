#!/bin/bash

./flow \
	--model cfg/yolov2-tiny-traffic-lights.cfg \
	--load -1 \
	--train \
	--trainer adam \
	--dataset data/bosch_dataset \
	--annotation data/bosch_dataset/annotations \
	--gpu 1.0



# ./flow --imgdir sample_img/ --model cfg/yolov2-tiny-traffic-lights.cfg --load -1