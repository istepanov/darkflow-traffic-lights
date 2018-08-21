FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update && \
	apt-get install -y wget libsm6 libxrender-dev libxtst6 python-setuptools
RUN pip install opencv-python PyYAML cython && python setup.py build_ext --inplace

WORKDIR /src
