#!/bin/bash

./flow \
	--model cfg/yolov2-tiny-traffic-lights.cfg \
	--load bin/tiny-yolo.weights \
	--train \
	--trainer adam \
	--dataset data/bosch_dataset \
	--annotation data/bosch_dataset/annotations \
	--gpu 1.0
