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

ret, thresh = cv2.threshold(gray, 80,150, cv2.THRESH_BINARY)

cv2.imshow("Outpur", thresh)
cv2.waitKey(0)

#Kontouren detektieren 

(cnts1,_) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
(cnts2,_) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Ändern auf 2 D Matrix

cnts1 = cnts1[0].reshape(-1,2)

cnts2 = cnts2[0].reshape(-1,2)

#Zeichene die Punkte als Kreise ein 

img1 = image.copy()
img2 = image.copy()


for (x,y) in cnts1:
	cv2.circle(img1,(x,y),1,(255,0,0),3)

for (x,y) in cnts2:
	cv2.circle(img2,(x,y),1,(255,0,0),3)

outPut = np.hstack([img1,img2])

cv2.imshow("Outpur", outPut)
cv2.waitKey(0)
cv2.destroyAllWindows()




