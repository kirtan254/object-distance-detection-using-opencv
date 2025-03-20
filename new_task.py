import cv2
import numpy as np

# Function to find the centroid of an object
def get_centroid(cnt):
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return (cx, cy)
    return None

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV ranges for red and blue colors
    lower_red1 = np.array([0, 120, 70])   # Lower bound for red (1st range)
    upper_red1 = np.array([10, 255, 255]) # Upper bound for red (1st range)
    
    lower_red2 = np.array([170, 120, 70])  # Lower bound for red (2nd range)
    upper_red2 = np.array([180, 255, 255]) # Upper bound for red (2nd range)

    lower_blue = np.array([100, 150, 50])  # Lower bound for blue
    upper_blue = np.array([140, 255, 255]) # Upper bound for blue

    # Create masks for red and blue objects
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2  # Combine both red masks

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours for both objects
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centroids = []

    # Process red object
    for cnt in contours_red:
        if cv2.contourArea(cnt) > 500:
            centroid = get_centroid(cnt)
            if centroid:
                centroids.append(centroid)
                cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)  # Red color
                cv2.circle(frame, centroid, 5, (0, 255, 255), -1)
                cv2.putText(frame, "Red", (centroid[0] + 10, centroid[1] - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Process blue object
    for cnt in contours_blue:
        if cv2.contourArea(cnt) > 500:
            centroid = get_centroid(cnt)
            if centroid:
                centroids.append(centroid)
                cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 2)  # Blue color
                cv2.circle(frame, centroid, 5, (0, 255, 255), -1)
                cv2.putText(frame, "Blue", (centroid[0] + 10, centroid[1] - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # If both objects are detected, calculate distance
    if len(centroids) == 2:
        (x1, y1), (x2, y2) = centroids
        distance = int(np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))  # Euclidean distance
        cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
        cv2.putText(frame, f"Distance: {distance} px", ((x1 + x2) // 2, (y1 + y2) // 2 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Display output
    cv2.imshow("Object Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
