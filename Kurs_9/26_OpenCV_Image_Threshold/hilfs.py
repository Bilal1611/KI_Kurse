import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Bild_IPhone.jpg")
#cv2.imshow("Bild",img)
#cv2.waitKey(0)

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




#Aus dem internet: step 51, maxValue =255, nrow = 3, ncols = maxValue// step
def loopThresh(image, step, maxValue, nrow, thresholdtype):
	nocols= maxValue/step
	i = 0
	#fig = plt.figure()
	fig, axs = plt.subplots(1,int(nocols)+1,figsize = (18,6))
	for thresh in range(0, maxValue, step):
		th,dst = cv2.threshold(image,thresh,maxValue, thresholdtype)
		#fig.add_subplot(nrow, nocols, i)
		print(i)
		axs[i].imshow(dst)
		axs[i].set_title(str(thresh))
		print(thresh)
		print(th)
		i = i+1
	plt.show()


def adploopThresh(image, step, maxValue,adaptiveMethod, thresholdtype,blocksize,paramter):
	nocols= maxValue/step
	i = 0
	#fig = plt.figure()
	fig, axs = plt.subplots(1,int(nocols)+1,figsize = (18,6))
	for thresh in range(0, maxValue, step):

		dst = cv2.adaptiveThreshold(image, thresh, adaptiveMethod, thresholdtype,blocksize,paramter)
		#fig.add_subplot(nrow, nocols, i)
		print(i)
		axs[i].imshow(dst)
		axs[i].set_title(str(thresh)+"Blocksize: {}, Paramter {}".format(str(blocksize), str(paramter)))
		print(thresh)
		i = i+1
	plt.show()


#loopThresh(img,51,255,3)

