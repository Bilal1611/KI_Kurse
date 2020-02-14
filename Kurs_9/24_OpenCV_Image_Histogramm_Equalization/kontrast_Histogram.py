import numpy as np 
import argparse 
import cv2 
import vg
import sys
from matplotlib import pyplot as plt 
from tkinter import *
from paket_mit_funktionen import*
import paket_mit_funktionen 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
print(paket_mit_funktionen.bot)
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

eq = cv2.equalizeHist(gray)
cv2.putText(gray,"Vorher",bot,fo,fs,fc,lt)
cv2.putText(eq,"nachher",bot,fo,fs,fc,lt)
cv2.imshow("Grau",gray)
cv2.imshow("Normal und Verbessert", np.hstack([gray,eq]))


cv2.imwrite(Bildname+ "Verbessert.jpg", eq)
cv2.imwrite(Bildname+ "Normal und Verbessert.jpg", np.hstack([gray,eq]))


cv2.waitKey(0)
