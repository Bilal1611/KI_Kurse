import numpy as np 
import argparse 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
cv2.imshow("Orginal", image)

# Abschneiden 
#Starte y:18 bis y:150, start x:57 bis x: 251
cropped = image[18:150, 57:251]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)




