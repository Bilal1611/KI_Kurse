from PIL import Image
import face_recognition
import numpy as np
import argparse
import cv2


# Abrufen der Argumente und Speichern im Wörterbuch
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# Laden und Konvertieren des Bildes in ein Numpy-Array
image = cv2.imread(args["image"])

# Finden Sie alle Gesichter im Bild mithilfe der Bibliothek
face_locations = face_recognition.face_locations(image)

# Gibt die Anzahl der Elemente im Array
print("I found {} face(s) in this photograph".format(len(face_locations)))

for face_location in face_locations:

	#Gibt die Position jedes Gesichts in diesem Bild
	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

	#Zeigt das Gesicht im Bild 
	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.show()

