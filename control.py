# import required modules

import cv2, pyautogui, mediapipe as mp

# capture video
video = cv2.VideoCapture(0)

# calling hand detection method from mediapipe
hand = mp.solutions.hands.Hands()

# for detecting landmarks on hand
handMarks = mp.solutions.drawing_utils

# capture frames from video
while True:
    _, frame = video.read()
    # frame flipping to get exact user side
    frame = cv2.flip(frame, 1)
    # convert frame to rgb
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # passing converted rgb frame for hand landmark detection
    height, width, _ = frame.shape
    screen_width, screen_height = pyautogui.size()
    processed = hand.process(rgb)
    # processing landmarks
    out = processed.multi_hand_landmarks
    y_index=0
    if out:
        # traverse through the coordinates
        for output in out:
            #  landmark coordinate values in the output frame
            # handMarks.draw_landmarks(frame, output)
            marks = output.landmark

            for num, mark in enumerate(marks):
                # marking x and y axis
                x_axis = int(mark.x * width)
                y_axis = int(mark.y * height)
                # detecting top point of index finger using id value
                if num == 8:
                    # circling around the point
                    cv2.circle(img=frame, center=(x_axis, y_axis), radius=20, color=(255,255,255))
                    if(y_axis<200):
                        pyautogui.press("volumeup")
                    elif(y_axis>200):
                        pyautogui.press("volumedown")
                    else:
                        pass
    frame= cv2.resize(frame, (960, 620))
    cv2.imshow('GestureControl',frame)
    if cv2.waitKey(1)==ord('q'):
        break



