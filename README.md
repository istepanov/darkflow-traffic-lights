## Intro

YOLO traffic light detection and classification, based on [Darkflow](https://github.com/thtrieu/darkflow).

### Requirements

* Docker
* nVidia Docker (if run on GPU)

### Build and run

* Download tensorflow checkpoint files from [here](https://drive.google.com/file/d/1RJBXxDPSK2H_m7psuaHoo0ESbZdWNVn5/view?usp=sharing) and extract them into `ckpt` folder.
* Run Docker container: `./docker-run-gpu.sh` (or `./docker-run-cpu.sh`)
* Run `./test.sh`
