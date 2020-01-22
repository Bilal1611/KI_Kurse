import numpy as np 
import argparse 
import flip 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
cv2.imshow("Orginal", image)


flipped = cv2.flip(image, 0)
cv2.imshow("Vertikal 0", flipped)

flipped = cv2.flip(image, 1)
cv2.imshow("Horizental 1", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Beide Flippen -1", flipped)

cv2.waitKey(0)
