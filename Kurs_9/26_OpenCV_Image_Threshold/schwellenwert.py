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
Bildname = args['image'][:-4]
#burred = np.stack([])


# Bild in Graustufen konvertieren 

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blurring implementieren
blurred = cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("Gauss Buller", blurred)
cv2.imwrite(Bildname + "Gauss Buller_Threshold.jpg", blurred)
#cv2.waitKey(0)


#Einfaches Thresholding 
(T, thresh) = cv2.threshold(blurred, 155,255, cv2.THRESH_BINARY)
#cv2.imshow("Threshold Binary", thresh)


#Simple Thresholding using inv binary 
(T, threshInv) = cv2.threshold(blurred, 155,255, cv2.THRESH_BINARY_INV)
#cv2.imshow("Threshold Inv Binary", threshInv)
#cv2.imshow("automatisch", cv2.bitwise_and(image, image, mask = threshInv))
#cv2.waitKey(0)


#adaptive thresholding using mean 
threshAM = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("adM4", threshAM)
#cv2.waitKey(0)

#adaptive thresholding using gaussian 
threshAG = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("adG4", threshAG)
cv2.waitKey(0)


threshAM1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,8)
cv2.imshow("adM8", threshAM1)
#cv2.waitKey(0)

#adaptive thresholding using gaussian 
threshAG1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,8)
cv2.imshow("adG8", threshAG1)
cv2.waitKey(0)
