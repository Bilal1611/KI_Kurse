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
Bildname = args['image'][:-4]
#burred = np.stack([])

# Average blurring 

blurred = np.hstack([
	cv2.blur(image, (3,3)),
	cv2.blur(image, (5,5)),
	cv2.blur(image, (7,7))])

cv2.imwrite(Bildname + "Average blur.jpg", blurred)

cv2.imshow("Average blurr", blurred)
cv2.waitKey(0)

# Gaussian blurring 

blurred = np.hstack([
	cv2.GaussianBlur(image, (3,3),0),
	cv2.GaussianBlur(image, (5,5),0),
	cv2.GaussianBlur(image, (7,7),0)])

cv2.imwrite(Bildname+ "Gaussian blurringr.jpg", blurred)

cv2.imshow("Gaussian blurr", blurred)
cv2.waitKey(0)


# Median blurring
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])

cv2.imwrite(Bildname+ "Median blurring.jpg", blurred)

cv2.imshow("Median blurring", blurred)
cv2.waitKey(0)

#Bilateral blurring 
blurred = np.hstack([
	cv2.bilateralFilter(image, 3,2,2),
	cv2.bilateralFilter(image, 5,31,310),
	cv2.bilateralFilter(image, 7,41,410)])

cv2.imwrite(Bildname+ "Bilateral blurring.jpg", blurred)

cv2.imshow("Bilateral blurring", blurred)
cv2.waitKey(0)

#

