from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # yolov8n = nano, yolov8s = small, yolov8m = medium, yolov8l = large, yolov8x = extra large
# better to use yolov8n because limitations of (pi)
# Training
model.train(
    data="data.yaml",       # path to dataset config yaml file of data set will be explained in how to create data set section
    epochs=100,             # number of training itrations (large data set == small epochs better to be from (30 to 50 )) || (small data set == more epochs (50 to 100))
    batch=16,               # batch size could be expalined as number of samples in one itration (in training process model moves by group of photos not 1 by 1) better to use small batch like 16 witch means slower training but it's suitable for weak gpu
    imgsz=640,              # input image size
    lr0=0.01,               # initial learning rate is the rate of updating model wieght keep it small to avoid overshooting
    optimizer="SGD",        # optimizer, choices: "SGD", "Adam", "AdamW" keep it SGD
    project="runs/train",   # folder to save results copy a empty folder path wich you want to keep your wights in it 
    name="exp",             # experiment name
    device=0,               # GPU index, -1 for CPU keep it 0 to use cuda and get fast and accurate results 
    workers=4,              # CPU threads 
    patience=50,            # early stopping patience thats mean if losses stuck or didn't enhance  for 50 epochs KILL training task
    cache=True,             # cache images for faster training
    verbose=True            # show training details
)
# you have to keep ur eye on loss, map and iou to tune your training 
# loss: is the diffrence between real boxes from manualy annotated data set and model prediction 
# MAP: is (mean average percision) it's important for informing accuracy of model 
# iou : is important for informing that the system is able to predict most targets  