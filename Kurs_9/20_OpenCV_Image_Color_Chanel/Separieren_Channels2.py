import numpy as np 
import argparse 
import cv2 
import vg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter Path to the Image")
args = vars(ap.parse_args())
# Bild hochladen
image = cv2.imread(args["image"])
#image = cv2.resize(image,(np.int(image.shape[1]/3),np.int(image.shape[0]/3)))
cv2.imshow("Orginal", image)

# Kanäle trennen
(B,G,R) = cv2.split(image)
print(R)
#BN = B/B.max()
#B = BN*255

#GN = G/G.max()
#G = GN*255


RN = R/R.max()
print(RN)
R = RN * 255

#print(R)

#cv2.imwrite("Test_Rot-Grue Normalized_mit_max.jpg", abs(cv2.subtract(R,G))
#cv2.imwrite("Test_Gruen-Rot Normalized_mit_max.jpg", abs(cv2.subtract(G,R))
#v2.imwrite("Test_Gruen-Rot Normalized_mit_max.jpg", abs(cv2.subtract(G,R))
#cv2.imwrite("Test_Blau-Rot Normalized_mit_max.jpg", abs(cv2.subtract(B,R))
#cv2.imwrite("Test_Rot-Blau Normalized_mit_max.jpg", abs(cv2.subtract(R,B))

cv2.imshow("Rot",R)
#cv2.imshow("Blau",B)
#cv2.imshow("Gruen",G)

cv2.waitKey(0)
