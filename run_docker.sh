#!/bin/bash

docker run  -p 6008:6008 --gpus all --shm-size=2gb -it -v /mnt/tv_developers/users/victor:/mnt/tv_developers/users/victor --name dinomc_v1.1 dinomc:v1.1
