import numpy as np 
import argparse 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])

#Ein Array erstellen und mit der Zahl 100 multplitzieren 
#Hier wird das Array addiert
M = np.ones(image.shape, dtype = "uint8")*100
added = cv2.add(image,M)
cv2.imshow("Addiert Image", added)

#Ein Array erstellen und mit der Zahl 100 multplitzieren 
#Hier wird das Array vom Bild substrahiert. 
M = np.ones(image.shape, dtype = "uint8")*50
added = cv2.subtract(image,M)
cv2.imshow("Subtrahiert image", added)
cv2.waitKey(0)
