import numpy as np 
import argparse 
import cv2 

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("mai of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around: {}".format(np.uint8([200])+ np.uint8([100])))
print("wrap aroung: {}".format((np.uint8([50])- np.uint8([100])))
