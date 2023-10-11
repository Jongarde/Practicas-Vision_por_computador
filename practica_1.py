import cv2
import numpy as np

point_collection = []

def draw_point_line(event, x, y, flags, param):
	global img
	if event == cv2.EVENT_LBUTTONDOWN:
		point_collection.append((x, y))
		cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
		tam = len(point_collection)
		if(tam > 1 and tam < 4):
			cv2.line(img, point_collection[tam-2], point_collection[tam-1], (0, 0, 255), 3) 
		elif(tam == 4):
			cv2.line(img, point_collection[tam-2], point_collection[tam-1], (0, 0, 255), 3) 
			cv2.line(img, point_collection[tam-1],point_collection[0], (0, 0, 255), 3)
			
		cv2.imshow('MyWindow', img)

def crop_selection(img, point_collection):
	points = np.array(point_collection)
	if len(point_collection) == 4:
		top_left_point = points.min(axis=0)
		bottom_right_point = points.max(axis=0)
		print(point_collection)
		print(top_left_point)
		print(bottom_right_point)
		cropped_img = img[top_left_point[1]:bottom_right_point[1],top_left_point[0]:bottom_right_point[0]]
		cv2.imshow("crop",cropped_img)
	else:
		print("You have to select 5 points!")

img = cv2.imread("Euros.jpg")

cv2.namedWindow('MyWindow')
cv2.imshow('MyWindow', img)
cv2.setMouseCallback('MyWindow', draw_point_line)
key = cv2.waitKey()
if key == ord('s') or key == 'S':
	crop_selection(img,point_collection)

exit_key = cv2.waitKey()
if key == 27:
	cv2.destroyAllWindows()
