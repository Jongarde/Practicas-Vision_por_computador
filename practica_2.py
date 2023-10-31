import cv2
import numpy as np

def convert_frame(frame):
	#img = cv2.pyrDown(cv2.imread("gorka.jpeg", cv2.IMREAD_UNCHANGED))
	img = cv2.resize(frame, (600, 600))

	img2 = cv2.GaussianBlur(img,(5,5),5,5)

	ret, thresh = cv2.threshold(cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY), 150, 255, cv2.THRESH_BINARY)
	contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	img_contorno=cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness = cv2.FILLED)
	ret2, thresh2=cv2.threshold(cv2.cvtColor(img_contorno,cv2.COLOR_BGR2GRAY),1,255,cv2.THRESH_BINARY)

	img_final=cv2.bitwise_and(img,img, mask=thresh2)

	ret3, thresh3=cv2.threshold(cv2.cvtColor(img_contorno,cv2.COLOR_BGR2GRAY),58,255,cv2.THRESH_BINARY)

	img_final2=cv2.bitwise_and(img_final,img_final, mask=thresh3)
	
	return img_final2

	#cv2.imshow("final",img_final2)

	#cv2.imshow("hull", img)
	#cv2.waitKey()

	# Limpiar después de cerrar la ventana
	#cv2.destroyAllWindows()
	

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	
	if not ret:
		print("Error")
		break
		
	img = convert_frame(frame)
	
	cv2.imshow("skin", img)
	
	if cv2.waitKey(1) and 0xFF == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()		
	
