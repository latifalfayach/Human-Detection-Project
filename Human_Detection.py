import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


## Histogram of Oriented Gradients Detector
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def Detector(frame,dc=0.65,c=0):
    ## USing Sliding window concept
    rects, weights = HOGCV.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=dc)
    drapo = 0
    c = len(pick) if c == 0 else c

    for x, y, w, h in pick:
        drapo += 1
        cv2.rectangle(frame, (x, y), (w, h), (139, 34, 104), 2)
        cv2.rectangle(frame, (x, y - 20), (w,y), (139, 34, 104), -1)
        cv2.putText(frame, f'P{drapo}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        if drapo == c:
            break

    cv2.putText(frame, f'Total Persons : {drapo}', (20, 450), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255,255), 2)
    
    return frame 
 