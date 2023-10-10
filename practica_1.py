import cv2
import numpy as np

point_collection = []

def draw_point_line(event, x, y, flags, param):
	global img

	if event == cv2.EVENT_LBUTTONDOWN:
		point_collection.append((x, y))
		cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
		tam = len(point_collection)
		if(tam > 1):
			cv2.line(img, point_collection[tam-2], point_collection[tam-1], (0, 0, 255), 3) 
		cv2.imshow('MyWindow', img)

img = cv2.imread("Euros.jpg")

cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', draw_point_line)

cv2.imshow('MyWindow', img)
cv2.waitKey()
cv2.destroyAllWindows()
