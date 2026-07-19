import time

import cv2
import numpy as np

import img_manip

w, h = 640, 480

def_frame = np.zeros((h, w, 3), dtype=np.uint8)
frame_full = def_frame.copy()

filename_full = "defult_full.jpg"

cap = cv2.VideoCapture(2, cv2.CAP_ANY)
if not cap.isOpened():
    print("Neuspesan pristup kameri!")
    exit()
else:
    print("Uspesan pristup kameri!")


cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

time.sleep(0.5)
for i in range(10):
    rez, frame_full = cap.read()

    if not rez:
        print("Neuspesna priprema!")
        exit()

print("Uspesna priprema!")

# Priprema OpenCV porozora koji ce da prikazuje live, ovo ne mora ali se radi kako bi se uklonio dodatan GUI
cv2.namedWindow("Live", cv2.WINDOW_GUI_NORMAL)
granica = 50
print("Pocinje kontinualno snimanje!")

while True:
    rez, frame_full = cap.read()

    if not rez:
        print("Bad frame!")
        continue

    cv2.imshow("Live", img_manip.bw_transform(frame_full, granica))

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:
        break
    elif key == ord("w"):
        granica += 10
    elif key == ord("s"):
        granica -= 10


print("Gotovo!")
cap.release()
cv2.destroyAllWindows()
