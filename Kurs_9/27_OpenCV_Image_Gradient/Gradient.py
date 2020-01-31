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

# Laplace gradient detektion 
lap = cv2.Laplacian(image, cv2.CV_64F)

# Konvertiert wieder zu 8 bit 
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplace Gradient Detection", lap)
cv2.imwrite(Bildname + "Laplace Gradient.jpg", lap)
cv2.waitKey(0)

#Sobel X and Y

sobelX = cv2.Sobel(image, cv2.CV_64F, 2, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 2)

#Konvertiere zurück zu 8 bit ohne unterschrift
sobelX = np.uint8(np.absolute(lap))
sobelY = np.uint8(np.absolute(lap))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)

cv2.imshow("Sobel Y", sobelY)

cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)



