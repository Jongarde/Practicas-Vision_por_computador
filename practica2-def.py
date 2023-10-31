import cv2
import numpy as np

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # 0 indicates the default camera (usually the built-in webcam)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error capturing the video feed.")
        break

    frame = cv2.resize(frame, (600, 600))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    limite_bajo = np.array([0, 91, 84], dtype=np.uint8)
    limite_alto = np.array([20, 180, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, limite_bajo, limite_alto)

    # Reduce noise with blur filters
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    skin = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Skin Detection', skin)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
