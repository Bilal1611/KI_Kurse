import numpy as np 
import argparse 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
image = cv2.resize(image,(np.int(image.shape[1]/3),np.int(image.shape[0]/3)))
cv2.imshow("Orginal", image)


#Rechteckige Maske erstellen
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (cX-75, cY -75), (cX+75, cY+75),255,-1)
cv2.imshow("Das ist unsere Rechteckmaske ", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
#masked = cv2.resize(masked,(np.uint8(cX/3),np.uint8(cY/3)))
cv2.imshow("Maskierter Rechteck Bild", masked )



#Kreisförmige Maske erstellen
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
cv2.circle(mask, (cX, cY), 100,255,-1)
cv2.imshow("Das ist unserer Kreis ", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
#masked = cv2.resize(masked,(np.uint8(cX/3),np.uint8(cY/3)))
cv2.imshow("Maskierter Kreis im Bild", masked )







cv2.waitKey(0)
