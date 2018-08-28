#!/bin/sh

set -e

docker build --build-arg TF_VERSION=latest -t istepanov/yolo-traffic-lights-cpu .
docker run -ti --rm -v `pwd`:/src istepanov/yolo-traffic-lights-cpu bash
