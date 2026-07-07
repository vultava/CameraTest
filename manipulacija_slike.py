# import datetime
import time

import cv2
import numpy as np

w, h = 640, 360
# d_t = datetime.datetime.now()

def_frame = np.zeros((h, w, 3), dtype=np.uint8)
frame_full = def_frame.copy()
frame_B = def_frame.copy()
frame_G = def_frame.copy()
frame_R = def_frame.copy()
frame_BW = def_frame.copy()
frame_bgr = def_frame.copy()


filename_full = "defult_full.jpg"
filename_B = "defult_B.jpg"
filename_G = "defult_G.jpg"
filename_R = "defult_R.jpg"
filename_BW = "defult_BW.jpg"
filename_bgr = "defult_bgr.jpg"

cap = cv2.VideoCapture(0, cv2.CAP_ANY)
if not cap.isOpened():
    print("Neuspesan pristup kameri!")
    exit()
else:
    print("Uspesan pristup kameri!")


cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

time.sleep(0.5)
for i in range(5):
    rez, frame_full = cap.read()

    if not rez:
        print("Neuspesno formiranje slike!")
        exit()

print("Uspesno slikanje!")

filename_full = "image_full.jpg"
cv2.imwrite(filename_full, frame_full)

cap.release()


for i in range(h):
    for j in range(w):
        # dekompozicija na b g r
        frame_B[i, j, 0] = frame_full[i, j, 0]
        frame_G[i, j, 1] = frame_full[i, j, 1]
        frame_R[i, j, 2] = frame_full[i, j, 2]

        # dekompozicija na crno i belo
        brig = round(
            (
                int(frame_full[i, j, 0])
                + int(frame_full[i, j, 1])
                + int(frame_full[i, j, 2])
            )
            / 3
        )

        if brig >= (255 / 2):
            frame_BW[i, j] = [255, 255, 255]
        else:
            frame_BW[i, j] = [0, 0, 0]

        # dekompozicija na uzastope b g r
        # !!! ako se kao operator izmedju i j koristi & ili | (bit-orijentisano I i ILI) dobija se serpinskijev trougao !!!
        if (i & j) % 3 == 0:
            frame_bgr[i, j, 0] = frame_full[i, j, 0]
        elif (i & j) % 3 == 1:
            frame_bgr[i, j, 1] = frame_full[i, j, 1]
        else:
            frame_bgr[i, j, 2] = frame_full[i, j, 2]

print("Gotova dekompozicija!")

filename_B = "image_B.jpg"
filename_G = "image_G.jpg"
filename_R = "image_R.jpg"
filename_BW = "image_BW.jpg"
filename_bgr = "image_bgr.jpg"

cv2.imwrite(filename_B, frame_B)
cv2.imwrite(filename_G, frame_G)
cv2.imwrite(filename_R, frame_R)
cv2.imwrite(filename_BW, frame_BW)
cv2.imwrite(filename_bgr, frame_bgr)
