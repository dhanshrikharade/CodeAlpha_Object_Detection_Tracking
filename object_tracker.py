
from ultralytics import YOLO
import cv2

# Load the YOLO object detection model
model = YOLO("yolo11n.pt")

# Open your laptop webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam could not be opened.")
    print("Check camera permissions and try again.")
    raise SystemExit

print("Object Detection and Tracking Started!")
print("Press Q to quit.")

while True:
    success, frame = cap.read()

    if not success:
        print("Could not read webcam frame.")
        break

    # Detect objects and track them across frames
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.35,
        imgsz=320, 
        verbose=False
    )
    # Display boxes, object names, and tracking IDs
    output_frame = results[0].plot()
    cv2.imshow("Object Detection and Tracking", output_frame)

    # Press Q to close the webcam window
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
