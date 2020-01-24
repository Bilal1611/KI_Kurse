import numpy as np 
import argparse 
import cv2 
import vg
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
#image = cv2.resize(image,(np.int(image.shape[1]/3),np.int(image.shape[0]/3)))
cv2.imshow("Orginal", image)
# Schneidet den String Minus 4. Also ist .jpg weg.
Bildname = args['image'][:-4]
Programmname = sys.argv[0][-13:-3]
# Kanäle trennen
(B,G,R) = cv2.split(image)

#cv2.imshow("Orginal R", R)
#cv2.imshow("Orginal B", B)
#cv2.imshow("Orginal G", G)

#cv2.waitKey(0) 

merged = cv2.merge([B,G,R])
cv2.imshow("Merged", merged)
#cv2.waitKey(0) 

#Alternative Methode 
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("ROT", cv2.merge([zeros,zeros,R]))
cv2.imshow("GREUN", cv2.merge([zeros,G,zeros]))
cv2.imshow("BLAU", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

