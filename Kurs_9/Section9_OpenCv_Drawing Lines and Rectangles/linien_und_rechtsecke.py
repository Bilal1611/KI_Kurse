import numpy as np
import cv2

# definiere eine Leihwand der Göße 300x300 Pixel mit 3 Channels 
#(R,G,B) Datentype der Größe 8 bit unter der Verwendung "unit8" 

canvas = np.zeros((300,300,3), dtype = "uint8")
# definiere Farbe
green = (0,255,0)
#Zeichne eine Linie 
cv2.line(canvas, (0,0), (300,300),green)
#Anzeigen des Leihwandes 
cv2.imshow("Die Leihwand", canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.line(canvas, (0,0), (300,300), red,3)
cv2.imshow("Die Leihwand", canvas)
cv2.waitKey(0)

# Zeichne ein Rechteck 
cv2.rectangle(canvas,(10,10), (60,60), green)
cv2.imshow("Rechteck auf der Leihwand", canvas)
cv2.waitKey(0)
