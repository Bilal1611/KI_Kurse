import argparse 
import cv2

#(1) Die Argmuente auswählen und speichern in einer dictionary 
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())
# Bild hochladen und oonvertieren in numpy Array
image = cv2.imread(args["image"])

(b,g,r) = image[0,0]
print("Pixel at (0,0)- Red: {}. Green: {}. Blue: {}" .format(r,g,b))

#(3)Set the pixel at 0,0 as Red(B,G,R)
image[0,0] = (0,0,255)
(b,r,g) = image[0,0]
print("Pixel at (0,0)- Red: {}. Green: {}. Blue: {}" .format(r,g,b))

#(4)Manipulating Pixel Regions 
#Grab a region of 100x100 pixels and show it in cv2 window 
#Start y, End y. Start x, End y as 0,100,0,100
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

#(5) Change the color of 100x100 pixels to green 
# Start y.End y.Start x.End x as 0,100 . 0, 100 respectively 
image[0:100, 0:100] = (0,255,0)
cv2.imshow("Update", image)
cv2.waitKey(0)


