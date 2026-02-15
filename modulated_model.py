import cv2
from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path="yolov8n.pt", device=0):
    
        self.model = YOLO(model_path)
        self.device = device

    def detect(self, frame, conf_threshold=0.3):
        results = self.model(frame)[0]  # run inference
        detections = [] # list to append detections box 

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # bounding box coords
            conf = float(box.conf[0])                # confidence
            cls_id = int(box.cls[0])                 # class id
            class_name = self.model.names[cls_id]   # class name

            if conf < conf_threshold:
                continue

            # draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            detections.append({
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "class_name": class_name, "conf": conf
            })

        return frame, detections

# Example usage
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # open default camera
    detector = YOLODetector(model_path="yolov8n.pt", device=0)

    while True:
        ret, frame = cap.read() # here you are capturing frames
        if not ret:
            break

        frame, dets = detector.detect(frame) # function detect takes frame from camera and returnes processed frame and detections list 
        print("Detections:", dets)

        cv2.imshow("YOLO Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # press ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()
