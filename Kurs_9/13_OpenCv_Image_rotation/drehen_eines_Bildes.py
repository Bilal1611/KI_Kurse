import numpy as np 
import argparse 
import rotation 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Orginal", image)

rotated = rotation.rotate(image,10)

cv2.imshow("Rotiert", rotated)
cv2.waitKey(0)