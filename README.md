since we are using ros so it's better to train model on linux
its better to use laptop with NVIDIA driver for training 
system requirments 
<img width="802" height="46" alt="Screenshot from 2026-02-15 02-34-47" src="https://github.com/user-attachments/assets/3d675307-2bb3-4216-8cec-2ba8310f0ef0" />
drivier instalation (you can skip if u have instaled one already ) 
from NVidia official website ("https://www.nvidia.com/en-us/drivers/")
chosse ur graphics card 
<img width="643" height="586" alt="Screenshot from 2026-02-15 02-38-03" src="https://github.com/user-attachments/assets/1d8925bc-8acc-4630-b16b-2a7d0c91a1fe" />
after downloading run the following commands for setup 
cd Downloads
chmod +x (delete this and write the name of the downloaded file) like == chmod +x NVIDIA-Linux-x86_64-580.126.09.run
sudo ./NVIDIA-Linux-x86_64-580.126.09.run
<img width="798" height="70" alt="Screenshot from 2026-02-15 02-56-09" src="https://github.com/user-attachments/assets/6fadff23-7314-43c3-ab21-15335da38b98" />
and it will open a gui for installation you can continue installation 
cuda installation 
cuda is an important tool for training your mode it ables you to train your model on gpu not cpu which is more faster and better accuarcy 
head to official nvidia cuda intallation web site (https://developer.nvidia.com/cuda/toolkit)


