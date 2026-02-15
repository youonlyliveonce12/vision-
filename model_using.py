import cv2
from ultralytics import YOLO

# Load pretrained YOLOv8 model
model = YOLO("here is the path of training wights (named with best wights)") 

cap = cv2.VideoCapture(0) # open laptop camera 

if not cap.isOpened(): #safity case to check if the camera is loaded 
    print("Cannot open camera")
    exit()

while True: # infinit loop for processing frames 
    ret, frame = cap.read() # ret checking if frame is grapped or not || frame is the processing frame
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO inference
    results = model(frame)[0] # take the first result  

    if results.boxes is not None: # if model returns results 
        for box in results.boxes: # boxes is object containes all boundry boxes that model predicted (for box in result.boxes : means processing each box )
            # x1,y1,x2,y2
            x1, y1, x2, y2 = map(int, box.xyxy[0]) # returns boundary box dimensions 
            conf = float(box.conf[0]) # returns level of confidence 
            cls_id = int(box.cls[0]) # returns class number 
            class_name = model.names[cls_id] # returns class name 

            # drawing boundary box 
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # parameters (frame is the processing image || x1,y1,x2,y2 = box dimensions || (0,255,0) box color here is green || 2 is thickness of box)
            cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1-10), # putting class name and level of confidence at upper corner of the box) 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2) # font style , color and thickness 

            # calculating box center
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # print class name , center and level of confidence
            print(f"{class_name} at center: ({cx}, {cy}), confidence: {conf:.2f}")

    # show image 
    cv2.imshow("YOLOv8 Detection", frame)

    # press q to exit task 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
