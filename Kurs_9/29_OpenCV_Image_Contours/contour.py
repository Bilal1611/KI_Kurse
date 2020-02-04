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

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Implementieren des Gaussian Blurr Filter 

blurred = cv2.GaussianBlur(gray, (5,5),0)
#kernl = np.ones((5,5),np.float32)/25

##blurred = cv2.filter2D(gray,-1, kernl)
cv2.imshow("Gaussian Blurr", blurred)

canny = cv2.Canny(blurred, 20, 40)
cv2.imwrite(Bildname + "Canny Edge.jpg", canny)
cv2.imshow("Canny Edge", canny)
cv2.waitKey(0)

#finding the contours, counting and marking them 
(cnts,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("The number of coins in in the Image is: {}".format(len(cnts)))

#Erstelle eine Kopie

contoursNr = image.copy()
#print(cnts)
# draw the countours in the actual color image copy
img1 = contoursNr
cnts1 = cnts[1].reshape(-1,2)
for (x,y) in cnts:
	print((x,y))
	cv2.circle(img1,(x,y),100,(255,0,0),3)

#cv2.drawContours(contoursNr,cnts,-1,(0,255,0),2)
#cv2.imshow("Cintours", contoursNr)
cv2.imshow("Cintours Cicle11", img1)
cv2.waitKey(0)

