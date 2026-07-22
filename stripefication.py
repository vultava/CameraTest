import cv2
import random

# Ucitavanje slike u Matlike
img_name = "dog.jpg"

img = cv2.imread(img_name)

if img is None:
    print("Image not loaded!")
    exit()

h, w, d = img.shape     # Dimnezije slike


# Promenljive-------------------
pix_num = 0
block = 0
randMin, randMax = 1, 50     # granice velicina bloka
row, col = 0, 0             # Koordinate "kursora"
#--------------------------------



while pix_num < (w*h):      # Radi loop dok se ne izvrsi operacija nad svim pikselima
    block = random.randint(randMin, randMax)

    # Kursor na kraju reda -> preskace u sledeci red
    if col == w:
        row +=1
        col = 0

    # Standardni slucaj kada operacija ne prelazi granice slike
    elif (col + block) <= w:
        pix_sum = [0, 0, 0]
        avg_c = [0, 0, 0]

        for pix in range(block):
            pix_sum += img[row, col + pix]

        avg_c = [round(pix_sum[0]/block), round(pix_sum[1]/block), round(pix_sum[2]/block)]

        for pix in range(block):
            img[row, col + pix] = avg_c

        col += block
        pix_num += block

    # Slucaj kada bi operacija bila izvrsena na nepostojecim piksleima van slike
    else:
        block = w - col
        pix_sum = [0, 0, 0]
        avg_c = [0, 0, 0]

        for pix in range(block):
            pix_sum += img[row, col + pix]

        avg_c = [round(pix_sum[0]/block), round(pix_sum[1]/block), round(pix_sum[2]/block)]

        for pix in range(block):
            img[row, col + pix] = avg_c

        col += block
        pix_num += block

cv2.namedWindow('Stripefied Image', cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow('Stripefied Image',w , h)
cv2.imshow('Stripefied Image', img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
