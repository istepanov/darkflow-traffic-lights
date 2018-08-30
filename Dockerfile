ARG TF_VERSION=latest-gpu

FROM tensorflow/tensorflow:${TF_VERSION}

RUN apt-get update && \
	apt-get install -y wget zip vim libsm6 libxrender-dev libxtst6 python-setuptools
RUN pip install opencv-python PyYAML cython plumbum

WORKDIR /src
