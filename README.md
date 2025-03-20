# Object Detection and Distance Measurement

This project uses OpenCV and NumPy to detect red and blue objects in a live webcam feed, find their centroids, and measure the distance between them in pixels.

## Features
- Detects red and blue objects in real-time.
- Draws contours around detected objects.
- Displays the centroid of each detected object.
- Calculates and displays the distance between two detected objects.

## Requirements
Make sure you have the following dependencies installed:

```sh
pip install opencv-python numpy
```

## Usage
1. Clone the repository or copy the script to your local machine.
2. Run the script using:
   ```sh
   python object_detection.py
   ```
3. Press **'q'** to exit the program.

## How It Works
- The script captures frames from the webcam.
- It converts the frame to the HSV color space.
- It applies color masking to detect red and blue objects.
- It finds contours of the detected objects and calculates their centroids.
- If two objects are detected, it calculates the Euclidean distance between them in pixels and displays it on the frame.

## Notes
- The distance displayed is in **pixels**. To convert it to centimeters, you need to perform camera calibration and determine the scale factor based on known object sizes.
- Ensure good lighting conditions for better object detection accuracy.

## License
This project is open-source and can be modified or distributed freely.

---

Feel free to modify the README as needed!
