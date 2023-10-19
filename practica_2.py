import cv2
import numpy as np
from scipy import ndimage

img = cv2.pyrDown(cv2.imread("gorka.jpeg", cv2.IMREAD_UNCHANGED))
img = cv2.resize(img,(600,600))
blurred = cv2.GaussianBlur(img, (11,11), 25,25)
#ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
limite_bajo = 60
limite_alto =  130

mask = cv2.inRange(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY), limite_bajo, limite_alto)
mask2 = cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), limite_bajo, limite_alto)

#mask2 = cv2.inRange(cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY), 90, 175)
# Apply the mask on the image to extract the original color
frame = cv2.bitwise_and(img, img, mask=mask)
frame2 = cv2.bitwise_and(img, img, mask=mask2)
cv2.imshow("hull", frame)
cv2.imshow("hullcity", frame2)
cv2.waitKey()
cv2.destroyAllWindows()