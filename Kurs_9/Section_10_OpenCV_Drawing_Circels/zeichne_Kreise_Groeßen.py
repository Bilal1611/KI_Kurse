import numpy as np
import cv2

#Erstellt eine Tafel
canvas = np.zeros((300,300,3), dtype ="uint8")
#Ordet die Farbe blau dem Array
blue = (255,00,00)
#Zeichnet einen Kreis im bereich 100 100
cv2.circle(canvas,(100,100),10,blue)

cv2.imshow("Das Programm zeichnet einen Kreis", canvas )
cv2.waitKey(0)

white = (255,255,255)

(centerX,centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
#Solange r zwischen 0 und 175 bitte, erhöhe r um 25 Pixel
for r in range(0,175,25):
	print(r)
	cv2.circle(canvas,(centerX,centerY),r,white)

cv2.imshow("Kreise", canvas)

cv2.waitKey(0)

