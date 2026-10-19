# Object Detection and Tracking

## CodeAlpha Internship — Task 4

### Project Overview
This project detects and tracks objects in real time using a webcam. It uses YOLO11 for object detection, OpenCV for video processing, and ByteTrack for tracking objects across video frames.

### Technologies Used
- Python
- YOLO11 (Ultralytics)
- OpenCV
- ByteTrack

### Features
- Real-time webcam object detection
- Object labels and bounding boxes
- Tracking IDs for detected objects
- Confidence-based detection filtering

### Project Structure

```text
ObjectDetectionTracking/
├── object_tracker.py
├── test_detection.py
├── requirements.txt
├── README.md
└── project_output.png
```

### Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Make sure the YOLO11n model file, `yolo11n.pt`, is available in the project folder.

### Run the Project

For real-time detection and tracking:

```bash
python object_tracker.py
```

For a single-frame detection test:

```bash
python test_detection.py
```

Press **Q** to close the real-time webcam window.

### Output
The application displays detected objects with bounding boxes, class labels, and tracking IDs.

See `project_output.png` for a screenshot of the application.

### Model
This project uses the pretrained YOLO11n model from Ultralytics.

### Internship
CodeAlpha Internship — Task 4: Object Detection and Tracking
