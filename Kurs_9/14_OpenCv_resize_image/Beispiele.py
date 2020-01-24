import numpy as np 
import argparse 
import cv2 
import vg
import sys

img = cv2.imread("cat.jpeg")
#cv2.imshow("Beispielbild", img)
(B,G,R) = cv2.split(img)
print(B.shape)
print(img.shape)
#cv2.waitKey(0)


