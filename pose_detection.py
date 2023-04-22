import cv2


def get_pose_landmarks(cap, pose):
    ret, frame = cap.read()
    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)

    return results.pose_landmarks
