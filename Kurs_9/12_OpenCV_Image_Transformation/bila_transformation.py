import numpy as np 
import argparse 
import translation 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orginal", image)

shifted = translation.translate(image,0,100)

cv2.imshow("Nach unten verschoben", shifted)
cv2.waitKey(0)
