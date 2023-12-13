# Use the official PyTorch image as the base image
# Ubuntu release 18.04.5 LTS
FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime
RUN echo "alias h=history" >> ~/.bashrc
RUN apt-get update
RUN apt-get install vim git -y
# For importing cv2:
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install --upgrade pip

# Set the working directory inside the container

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install any dependencies specified in requirements.txt
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /mnt/tv_developers/users/victor/DINO-MC

# Set the entry point to bash
ENTRYPOINT ["/bin/bash"]
