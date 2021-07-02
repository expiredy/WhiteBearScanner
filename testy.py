import numpy as np

import cv2


image = cv2.imread(input())
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
# display the results of the naive attempt
cv2.imshow("Naive", image)
# apply a Gaussian blur to the image then find the brightest
# region
gray = cv2.GaussianBlur(gray, (10, 10), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()
cv2.circle(image, maxLoc, 10, (255, 0, 0), 2)

# display the results of our newly improved method
cv2.imshow("Robust", image)
cv2.waitKey(0)