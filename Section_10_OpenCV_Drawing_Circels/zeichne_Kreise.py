import numpy as np
import cv2

#Erstellt eine Tafel
canvas = np.zeros((300,300,3), dtype ="uint8")
#Ordet die Farbe blau dem Array
blue = (255,00,00)
#Zeichnet einen Kreis
cv2.circle(canvas,(100,100),10,blue)

cv2.imshow("Das Programm zeichnet einen Kreis", canvas )
cv2.waitKey(0)