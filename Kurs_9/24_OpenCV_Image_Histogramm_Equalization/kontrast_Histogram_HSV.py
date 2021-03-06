import numpy as np 
import argparse 
import cv2 
import vg
import sys
from matplotlib import pyplot as plt 
from tkinter import *

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
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(imageHSV)
cv2.imwrite(Bildname +"Grau"+ ".jpg", gray)

cv2.imshow("Grau",gray)

eq = cv2.equalizeHist(gray)
h = cv2.equalizeHist(h)
s = cv2.equalizeHist(s)
v = cv2.equalizeHist(v)
hsv = cv2.merge([h,s,v])
eqq = cv2.merge([eq,eq,eq])
cv2.imshow("Normal und Verbessert", np.hstack([hsv,eqq]))

cv2.imwrite(Bildname+ "Verbessert.jpg", eq)
cv2.imwrite(Bildname+ "Normal und Verbessert HSV.jpg", np.hstack([hsv,eqq]))


cv2.waitKey(0)
