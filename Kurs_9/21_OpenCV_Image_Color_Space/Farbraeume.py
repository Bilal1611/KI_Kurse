import numpy as np 
import argparse 
import cv2 
import vg
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
#Zeigt ein normales Image
cv2.imshow("RGB Colour space", image)
#cv2.waitKey(0)
Bildname = args['image'][:-4]


# RGB verwandeln zu Grau
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(Bildname +"Grau"+ ".jpg", gray)
cv2.imshow("Grau",gray)

# BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite(Bildname+"HSV"+".jpg", hsv)
cv2.imshow("HSV",hsv)

# BGR to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imwrite(Bildname+"LAB"+".jpg", lab)
cv2.imshow("LAB", lab)

cv2.waitKey(0)


