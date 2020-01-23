import numpy as np 
import argparse 
import cv2 

# Erstellen eines Rechteckes 

rectangle = np.zeros((300,300), dtype = "uint8")
#Füllen eines Rechteckes
cv2.rectangle(rectangle, (25,25), (275,275),255,-1)
cv2.imshow("Rechteck gefuellt mit 255", rectangle)

#Erstellen eines Kreises
circle = np.zeros((300,300), dtype = "uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("Hier wurde kein Operator verwendet", circle)

# Bitoperationen durchführen 

#Adiieren
bitwiseAnd = cv2.bitwise_and(rectangle,circle)
cv2.imshow("Hier wurde der Operator And verwendet", bitwiseAnd)
cv2.waitKey(0)


#Oderieren 
bitwiseOr = cv2.bitwise_or(rectangle,circle)
cv2.imshow("Hier wurde der Operator Or verwendet", bitwiseOr)
cv2.waitKey(0)


#Xoriern  
bitwiseXor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("Hier wurde der Operator xor verwendet", bitwiseXor)
cv2.waitKey(0)

#Notieren  
bitwiseNor = cv2.bitwise_not(rectangle,circle)
cv2.imshow("Hier wurde der Operator not verwendet", bitwiseXor)
cv2.waitKey(0)




