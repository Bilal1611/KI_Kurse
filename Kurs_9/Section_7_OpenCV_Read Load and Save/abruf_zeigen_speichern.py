import argparse 
import cv2

# Die Argmuente auswählen und speichern in einer dictionary 
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())
# Bild hochladen und oonvertieren in numpy Array
image = cv2.imread(args["image"])
print("width of the image in pixels is: {}".format(image.shape[1]))
print("Hight of the image in pixels is: {}".format(image.shape[0]))
print("Channels of the image in pixels is: {}".format(image.shape[2]))

# Load image into cv2 window 
#wait for key press
# Bild in einem anderem Format abspeichern 
cv2.imshow("Image Title", image)
cv2.waitKey(5000)
cv2.imwrite("newcat.jpg")
