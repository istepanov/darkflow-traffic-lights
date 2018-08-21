#!/bin/sh

set -e

docker build -t istepanov/yolo-traffic-lights .
docker run --runtime=nvidia -ti --rm -v `pwd`:/src istepanov/yolo-traffic-lights bash
