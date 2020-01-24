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
cv2.imwrite(Bildname +"Grau"+ ".jpg", gray)
cv2.imshow("Grau",gray)

#Erstelle ein Histogram 
hist = cv2.calcHist([gray],[0],None,[256],[0,256])
#Grafik erstellen 
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("No of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

