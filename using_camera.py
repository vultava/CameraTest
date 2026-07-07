import time

import cv2
import numpy

capture_object = cv2.VideoCapture(
    0, cv2.CAP_ANY
)  # napravi objekat koji predstavlja kameru


# proverava da li je kamera otvorena kako treba
if capture_object.isOpened():
    print("Camera opened!")
else:
    print("Camera could not be opened!")
    exit()


# dimenzije slike
w = 640
h = 360
capture_object.set(cv2.CAP_PROP_FRAME_WIDTH, w)
capture_object.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

# treba malo sacekati da se kamera normalizuje
time.sleep(2)

# ako ne uspe da napravi sliku eksportovace samo crnu sliku
frame = numpy.zeros((h, w, 3), dtype=numpy.uint8)

# slika pet puta kako bi se namestio ekspouzr i tk to
for i in range(5):
    ret, frame = capture_object.read()

    # file_name = f"image{i}.jpg"
    # cv2.imwrite(file_name, frame)
    if not ret:
        print("Reading unsuccessful!")
        exit()

file_name = "image.jpg"
cv2.imwrite(file_name, frame)

capture_object.release()
