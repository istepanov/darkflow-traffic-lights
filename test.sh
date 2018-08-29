#!/bin/bash

python setup.py build_ext --inplace

./flow \
    --imgdir sample_img/ \
    --model cfg/yolov2-tiny-traffic-lights.cfg \
    --threshold 0.5 \
    --load -1
