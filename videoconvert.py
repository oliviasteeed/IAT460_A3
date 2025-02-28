import cv2
import numpy as np
import time

# disclaimer: I used ChatGPT to assist (as was encouraged in lab) since I am not well versed in video manipulation with Python

print("######## NEW RUN #########")

# load video
video_path = "/Users/oliviasteed/Desktop/original_videos/layer9.mp4"
cap = cv2.VideoCapture(video_path)

# getting video details
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))    # get fps

# define output video writer
out = cv2.VideoWriter('/Users/oliviasteed/Desktop/edited_videos/layer9_1.mp4', 
                      cv2.VideoWriter_fourcc(*'mp4v'), 
                      fps, (frame_width, frame_height), 
                      isColor=False)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No frame read, exiting...")
        break

    # convert grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # normalize brightness levels 
    gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

    # get min and max pixel values of video
    min_value = int(np.min(gray))  
    max_value = int(np.max(gray))  

    # calculate threshold (under is black, over is white)
    threshold_val = (min_value + max_value) // 2  # Compute midpoint safely

    # apply threshold 
    _, binary = cv2.threshold(gray, threshold_val, 255, cv2.THRESH_BINARY)

    out.write(binary)

    # add delay (otherwise it skips frames)
    time.sleep(1 / fps)  

cap.release()
out.release()
cv2.destroyAllWindows()
