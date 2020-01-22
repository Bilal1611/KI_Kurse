import numpy as np 
import argparse 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
# Hier werden zwei Array addiert.
print("max of 255 by Cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 255 by Cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))