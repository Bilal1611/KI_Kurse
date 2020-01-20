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
#Generiere Zufallskreise gefüllt. 

for i in range(0,25):
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high = 256, size = (3,)).tolist()
	pt = np.random.randint(0,high=300,size = (2,))
	cv2.circle(canvas, tuple(pt), radius,color, -1)

	print(i)
	

cv2.imshow("Kreise generiert nach Zufall", canvas)

cv2.waitKey(0)

