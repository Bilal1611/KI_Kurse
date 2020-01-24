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
#Zeigt ein Bild
cv2.imshow("RGB Colour space", image)
#cv2.waitKey(0)
Bildname = args['image'][:]

# Hier wird das Bild in RGB-Kanäle gesplittet
chans = cv2.split(image)

# Erstelle ein Tyuple für die Vorschleife, 
#um Hist in Farben zu plotten
colors = ("b", "g", "r" )
#grafikdarstellung 
plt.figure()
plt.title("Histogram in Farben")
plt.xlabel("Bins")
plt.ylabel("No of pixels")

for(chan,color) in zip(chans, colors):
	#Bei jedem Schleifendurchlauf wird ein Histogram erstellt
	hist = cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist, color = color)
	plt.xlim([0,256])

plt.savefig("Histogram" + Bildname )
plt.show()
cv2.waitKey(0)