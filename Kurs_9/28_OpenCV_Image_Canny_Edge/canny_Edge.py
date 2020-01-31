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

# Implementieren des Gaussian Blurr Filter 

blurred = cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("Gaussian Blurr", blurred)

canny = cv2.Canny(blurred, 20, 150)
cv2.imwrite(Bildname + "Canny Edge.jpg", canny)
cv2.imshow("Canny Edge", canny)
cv2.waitKey(0)
