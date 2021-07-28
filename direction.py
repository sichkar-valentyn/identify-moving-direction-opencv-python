

# Importing needed libraries
import cv2
import argparse
import numpy as np

from collections import deque


"""
Start of:
Preparing arguments
"""

# Constructing the argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', type=str, default='test.mov', help='Specify path to the video file')

# Parsing the arguments
args = vars(ap.parse_args())

"""
Start of:
Preparing arguments
"""

"""
Start of:
Initializing tracker
"""

# Initializing tracker
# tracker = cv2.TrackerCSRT_create()
tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerTLD_create()
# tracker = cv2.TrackerMedianFlow_create()
# tracker = cv2.TrackerMOSSE_create()

"""
End of:
Initializing tracker
"""


"""
Start of:
Preparing OpenCV windows to be shown
"""

# Giving names to the windows
# Specifying that windows are resizable

# Window to show current view from camera in Real Time
cv2.namedWindow('Current view', cv2.WINDOW_NORMAL)

# Window to show spent time to process current frame
cv2.namedWindow('Direction', cv2.WINDOW_NORMAL)

"""
End of:
Preparing OpenCV windows to be shown
"""


"""
Start of:
Reading frames from camera in the loop
"""

# Defining 'VideoCapture' object
video = cv2.VideoCapture(args['video'])

# Initializing ROI to be tracked
roi = None

# Initializing variables for spatial dimensions of the captured frames
h, w = None, None

# Initializing deque object for center points of the detected object
points = deque(maxlen=50)

# Creating image with black background
temp = np.zeros((720, 1280, 3), np.uint8)


# Defining loop to catch frames
while True:
    # Capturing frames one-by-one from video file
    _, frame_bgr = video.read()

    # If the frame was not retrieved
    # e.g.: at the end of the video,
    # then we break the loop
    if not _:
        break

    # Getting spatial dimension of the frame
    # We do it only once from the very beginning
    # All other frames have the same dimensions
    if w is None or h is None:
        # Getting shape of the caught frame
        (h, w) = frame_bgr.shape[:2]

        # Select needed area and press ENTER or SPACE
        roi = cv2.selectROI('Current view', frame_bgr, fromCenter=False, showCrosshair=True)

        # Initializing OpenCV object tracker
        tracker = cv2.TrackerKCF_create()
        tracker.init(frame_bgr, roi)

    # Selecting ROI to track the needed object
    if cv2.waitKey(10) & 0xFF == ord('r'):
        # Updating queue with center points
        points.clear()

        # Select needed area and press ENTER or SPACE
        roi = cv2.selectROI('Current view', frame_bgr, fromCenter=False, showCrosshair=True)

        # Initializing OpenCV object tracker
        tracker = cv2.TrackerKCF_create()
        tracker.init(frame_bgr, roi)

    # Tracking the object
    if roi is not None:
        # Getting new bounding box coordinates of the tracked object
        (success, box_coordinates) = tracker.update(frame_bgr)

        # Visualizing bounding box if it was obtained
        if success:
            # Extracting bounding box coordinates as integer numbers
            (x_min, y_min, box_width, box_height) = [int(c) for c in box_coordinates]

            # Drawing rectangle around the object
            cv2.rectangle(frame_bgr,
                          (x_min, y_min),
                          (x_min + box_width, y_min + box_height),
                          (0, 255, 0),
                          3)

            # Getting current center coordinates of the bounding box
            center = (int(x_min + box_width / 2), int(y_min + box_height / 2))

            # Adding current pont to the queue
            points.appendleft(center)

        # In case no bounding box is obtained, clear the queue
        else:
            # Updating queue with center points
            points.clear()

        # Visualizing tracking line
        for i in range(1, len(points)):
            # If no points collected yet
            if points[i - 1] is None or points[i] is None:
                continue

            # Draw the line between points
            cv2.line(frame_bgr, points[i - 1], points[i], (0, 255, 0), 3)

            # Changing background to BGR(230, 161, 0) in the additional window
            # B = 230, G = 161, R = 0
            temp[:, :, 0] = 230
            temp[:, :, 1] = 161
            temp[:, :, 2] = 0

            # Adding text to the additional window
            cv2.putText(temp,
                        'Direction',
                        (100, 200),
                        cv2.FONT_HERSHEY_TRIPLEX,
                        6,
                        (255, 255, 255),
                        6,
                        cv2.LINE_AA)

            # Drawing arrow on the additional window
            start_point = points[-1]
            end_point = points[0]
            cv2.arrowedLine(temp, start_point, end_point, (0, 255, 0), 10, cv2.LINE_AA, 0, 0.3)

        # Showing image with spent time for 2D convolution for current frame
        cv2.imshow('Direction', temp)

    # Showing current view from camera in Real Time
    # Pay attention! 'cv2.imshow' takes images in BGR format
    cv2.imshow('Current view', frame_bgr)

    # Breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Releasing 'VideoCapture' object
video.release()

# Destroying all opened OpenCV windows
cv2.destroyAllWindows()
