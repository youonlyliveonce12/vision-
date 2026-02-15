## data set structure 
<img width="168" height="633" alt="Screenshot from 2026-02-15 06-49-52" src="https://github.com/user-attachments/assets/ed2cdf35-ed21-4098-8f51-33964e9cb7c9" />

## How to label image 

after downloading labelImg python program (expalined in readme) 

cd labelImg

python3 labelImg.py

will open like that 

<img width="1920" height="1080" alt="Screenshot from 2026-02-15 06-10-58" src="https://github.com/user-attachments/assets/e32a8136-15ee-4350-9454-60fa4dfbafdc" />

make 2 folders for images and labels 

<img width="355" height="139" alt="Screenshot from 2026-02-15 06-18-04" src="https://github.com/user-attachments/assets/e2af72b6-faeb-4a88-bb6e-382dc5aba89f" />

click on open dir and choose ur images direction 

<img width="183" height="139" alt="Screenshot from 2026-02-15 06-16-23" src="https://github.com/user-attachments/assets/331b31fd-f3eb-471e-b9d9-f377e894c016" />

<img width="635" height="454" alt="Screenshot from 2026-02-15 06-21-04" src="https://github.com/user-attachments/assets/c5843b62-f7ac-4088-be0a-ea078c9ba941" />

toggele here and choose yolo

<img width="164" height="263" alt="Screenshot from 2026-02-15 06-36-23" src="https://github.com/user-attachments/assets/44998c7d-e6cf-4c7f-9be3-6e7fa1f8be51" />

click on rectBox and draw a box around your detection target and type or choose the object class (object name )

<img width="1920" height="1080" alt="Screenshot from 2026-02-15 06-23-01" src="https://github.com/user-attachments/assets/c1593a89-2b3d-4103-bc96-374db7b1620f" />

click on file and change save dir then choose ur labels folder 

<img width="1920" height="1080" alt="Screenshot from 2026-02-15 06-27-05" src="https://github.com/user-attachments/assets/e9eb8039-9d37-4b99-9c11-e67bd9e0aad8" />

click on verify image and save the label of image will be saved in labels folder 

click on next and do the same for the next image 

note labels will be saved in order like that 

<img width="699" height="138" alt="image" src="https://github.com/user-attachments/assets/a2267b96-c4d2-4880-8172-373bb3cb0f6c" />

choose 80 % of your dataset for training and 20% for testing

now creat data.yaml file 

train: dataset/train/images # here put ur train images folder direction 

val: dataset/val/images    # here put ur val  images folder direction 

test: dataset/test/images  # here put ur test images folder direction 

nc: 3 # number of classes u have 

names: ['bottle', 'cup', 'box'] # name of ur classes 

note : you can put val and test the same direction 

## date set example 

https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw

if you found your target dataset here no need for creating one 



