import cv2
import numpy as np

point_collection = []
region_collection = []

def draw_point_line(event, x, y, flags, param):
	global img, point_collection
	if event == cv2.EVENT_LBUTTONDOWN:	
		point_collection.append((x, y))
		cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
		tam = len(point_collection)
		if(tam > 1):
			if(tam%4 == 0):
				cv2.line(img, point_collection[tam-2], point_collection[tam-1], (0, 0, 255), 3) 
				cv2.line(img, point_collection[tam-1],point_collection[tam-4], (0, 0, 255), 3)
				region_collection.append(point_collection)
				point_collection = []
			elif(tam%4 == 1):
				pass
			else:
				cv2.line(img, point_collection[tam-2], point_collection[tam-1], (0, 0, 255), 3) 			
		cv2.imshow('MyWindow', img)

def crop_selection(img, point_collection):
	for i, region in enumerate(region_collection):
		if len(region) == 4:
			points = np.array(region)
			top_left_point = points.min(axis=0)
			bottom_right_point = points.max(axis=0)
			cropped_img = img[top_left_point[1]:bottom_right_point[1],top_left_point[0]:bottom_right_point[0]]
			cv2.imwrite("crop" + str(i) + ".jpg", cropped_img)
		else:
			print("You have to select 4 points for each region!")

img = cv2.imread("Euros.jpg")

cv2.namedWindow('MyWindow')
cv2.imshow('MyWindow', img)
cv2.setMouseCallback('MyWindow', draw_point_line)
key = cv2.waitKey()
if key == ord('s') or key == ord('S'):
	crop_selection(img,point_collection)
	for i in range(len(region_collection)):
		print("crop" + str(i) + ".jpg")
		cv2.imshow("Crop",cv2.imread("crop" + str(i) + ".jpg"))

exit_key = cv2.waitKey()
if key == 27:
	cv2.destroyAllWindows()
