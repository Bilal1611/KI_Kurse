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
Programmname = sys.argv[0][-9:-3]
# Kanäle trennen
(B,G,R) = cv2.split(image)
cv2.imshow("Orginal", R)
cv2.imshow("Orginal", B)
cv2.imshow("Orginal", G)
#BN = B/np.linalg.norm(B)
#B = BN

#GN = G/np.linalg.norm(G)
#G = GN

#RN = R/np.linalg.norm(R)
#R = RN

cv2.imwrite(Bildname+"Rot-Blau"+Programmname+".jpg", R-B)
cv2.imwrite(Bildname+"_Blau-Rot"+Programmname+".jpg", B-R)
cv2.imwrite(Bildname+"_Gruen-Blau"+Programmname+".jpg", G-B)
cv2.imwrite(Bildname+"_Blau-Rot"+Programmname+".jpg", B-G)
#cv2.imwrite(Bildname+"Ref_Rot-Blau Normalized"+Programmname+".jpg", cv2.subtract(np.uint8(R),np.uint8(B)))

#cv2.imwrite(Bildname+"_Ref_Rot-Grue"+Programmname+".jpg", cv2.subtract(np.uint8(R),np.uint8(G)))
#cv2.imwrite(Bildname+"_Ref_Gruen-Rot Normalized"+Programmname+".jpg", cv2.subtract(np.uint8(G),np.uint8(R)))
#cv2.imwrite(Bildname+"_Ref_Blau-Rot Normalized"+Programmname+".jpg", cv2.subtract(np.uint8(B),np.uint8(R)))
#cv2.imwrite(Bildname+"Ref_Rot-Blau Normalized"+Programmname+".jpg", cv2.subtract(np.uint8(R),np.uint8(B)))




cv2.imshow("Rot",R-B)
cv2.imshow("Blau",B-R)
cv2.imshow("Gruen",G-B)
cv2.imshow("Gruen",B-G)

cv2.waitKey(0)
