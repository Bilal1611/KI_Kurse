import numpy as np 
import cv2



bottomLeftCornerOfText =(0,20)
bot = bottomLeftCornerOfText


font = cv2.FONT_HERSHEY_SIMPLEX 
fo = font

fontScale = 1
fs = fontScale

fontColor = (0,255,0)
fc = fontColor

lineType = 2
lt = lineType

fig = plt.figure()

def loopThresh(image, step,maxValue,nrow, nocols = maxValue//step):
	i = 1

	for thresh in range(0, maxValue, step):
		th,dst = cv2.threshhold(image,thresh,maxValue, cv2.THRESH_BINARY)
		fig.add_subplot(nrow, ncols, i)
		plt.imshow(dst)
		
		i = i+1

