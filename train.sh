#!/bin/bash

python setup.py build_ext --inplace

./flow \
	--model cfg/yolov2-tiny-traffic-lights.cfg \
	--load -1 \
	--train \
	--trainer adam \
	--dataset data/bosch/images \
	--annotation data/bosch/annotations \
	--gpu 1.0
