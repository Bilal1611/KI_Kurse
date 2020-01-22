
import numpy as np 
import cv2 

def resizing(image, width=None, height = None, inter = cv2.INTER_AREA):
	dim = None 
	# Erhält die Liste als werte der Höhe und Breite in Pixel.
	(h,w) = image.shape[:2]
	# wenn die Breite und Höhe nicht vorgegebn sind, dann soll das Bild nur geliefert werden
	if width is None and height is None:
		return image
	# Wenn aber nur die Höhe aber nicht die Breite vorgegeben ist, 
	#dann soll r als das Verhältnis von der gewünschten Höhe und 
	#der ürsprünglichen Bildbreite berechnet werden.

	if width is None:
		r = height/ float(h)
		dim = (int(w*r),height)
	# Im anderen Fall soll r entsprechend berechnet werden
	else: 
		r = width/float(w)
		dim = (width,int(h*r))
	resized = cv2.resize(image, dim, interpolation = inter)

	return resized

