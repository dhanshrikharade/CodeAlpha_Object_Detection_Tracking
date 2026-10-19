
from ultralytics import YOLO
import cv2

print("Loading model...")
model = YOLO("yolo11n.pt")

print("Opening webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Webcam unavailable")
    raise SystemExit

print("Reading one frame...")
success, frame = cap.read()
cap.release()

if not success:
    print("ERROR: Could not read webcam")
    raise SystemExit

print("Detecting objects... Please wait.")
results = model.predict(frame, imgsz=320, verbose=False)

output = results[0].plot()
cv2.imshow("Detection Test", output)
print("Detection complete! Press any key in the image window to close.")
cv2.waitKey(0)
cv2.destroyAllWindows()
