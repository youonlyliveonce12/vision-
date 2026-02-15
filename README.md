# YOLOv8 + ROS2 Setup Guide

This guide helps you set up **YOLOv8** with **ROS2 ** on Ubuntu 22.04/24.04 using NVIDIA GPU for fast training and inference.

---

##  System Requirements

- Ubuntu 22.04 or 24.04  
- NVIDIA GPU (laptop or desktop)  
- At least 6GB GPU memory recommended  
- Internet connection

**Example:**

![System](https://github.com/user-attachments/assets/3d675307-2bb3-4216-8cec-2ba8310f0ef0)

---

## Install NVIDIA Driver

Download the latest driver from [NVIDIA Official Website](https://www.nvidia.com/en-us/drivers/) for your GPU.  

After downloading, run:

cd ~/Download
chmod +x NVIDIA-Linux-x86_64-580.126.09.run
sudo ./NVIDIA-Linux-x86_64-580.126.09.run

## Install CUDA
Ubuntu 22.04 → CUDA 12.6

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda-repo-ubuntu2204-12-6-local_12.6.0-560.28.03-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-6-local_12.6.0-560.28.03-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6

Ubuntu 24.04 → CUDA 13

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin
sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget https://developer.download.nvidia.com/compute/cuda/13.1.1/local_installers/cuda-repo-ubuntu2404-13-1-local_13.1.1-590.48.01-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2404-13-1-local_13.1.1-590.48.01-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2404-13-1-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo apt-get update
sudo apt-get -y install cuda-toolkit-13-1

## Set CUDA Environment Variables
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

## Install Python 3.10

sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-dev python3.10-distutils

python3 --version
# Should return Python 3.10.x

Install Numpy (<2 recommended)
# Remove pre-installed numpy if exists
sudo apt remove python3-numpy

# Upgrade pip
python3.10 -m pip install --upgrade pip

# Install numpy < 2
python3.10 -m pip install "numpy<2"
install PyTorch
For CUDA 12.6
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126

For CUDA 13
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130


## Test installation:

import torch
print(torch.cuda.is_available())  # True
print(torch.version.cuda)         # Should match your CUDA version

## Install YOLOv8
# Stable version
pip install -U ultralytics

# Or from GitHub main branch
pip install git+https://github.com/ultralytics/ultralytics.git@main









