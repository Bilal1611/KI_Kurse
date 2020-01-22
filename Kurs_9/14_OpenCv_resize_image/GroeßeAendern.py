import numpy as np 
import argparse 
import resize 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Orginal", image)

resized1 = resize.resizing(image, width = 100)
cv2.imshow("Groeße um 100 veraendert", resized1)

resized = resize.resizing(image, height = 100)
cv2.imshow("Hoehe um 10 veraendert", resized)

cv2.waitKey(0)