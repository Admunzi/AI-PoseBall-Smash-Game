"""
Pose Detection

This class is going to be used to detect the pose landmarks on the webcam.
We will use the track pose function from mediapipe to detect the pose landmarks and draw them on game screen.

"""
import cv2


def get_pose_landmarks(cap, pose):
    ret, frame = cap.read()
    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)

    return results.pose_landmarks
