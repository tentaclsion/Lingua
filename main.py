# might be a good tutorial to follow
# https://pythonexamples.org/python-opencv-write-text-on-image-puttext/
import numpy as np
import cv2

# if we want to test webcam stuff
# cam = cv2.VideoCapture(0)
# ret_val, image = cam.read()

# create a 720p black image
image = np.zeros((720, 1280))
width, height = image.shape
print(width, height)

# other variables
text = "test"
font = cv2.FONT_HERSHEY_SIMPLEX # might want to include a font in the final product, default ones suck
font_size = 2.5
text_color = (255, 255, 255)
font_weight = 2

# place text in the center of the image
textsize = cv2.getTextSize(text, font, font_size, font_weight)[0]
position = ((int) (image.shape[1]/2 - textsize[0]/2), (int) (image.shape[0]/2 - textsize[1]/2))

# place text on image
cv2.putText(image, text, position, font, font_size, text_color, font_weight)

# show image in frame
cv2.imshow("", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lingua encompasses a broad spectrum of applications ranging from professional business settings to casual meetings with family and friends. As a result, it is intended for a wide variety of people, essentially, those who frequent online calls or presentations in all kinds of settings with a need to provide real-time translation. For example, this could be college professors broadcasting their lectures to the public, or even an international business meeting between two companies discussing acquisitions.");

# webcam stuff
# while True:
# 	ret_val, image = cam.read()
# 	cv2.putText(image, text, position, font, font_size, text_color, font_weight)
# 	cv2.imshow('Webcam', image)
# 	if cv2.waitKey(1) == 27:
# 		break  # esc to quit
# cv2.destroyAllWindows()