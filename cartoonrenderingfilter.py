import cv2 as cv
import numpy as np


img = cv.imread('img.jpg')
grayimg = cv.imread('img.jpg', cv.IMREAD_GRAYSCALE)
grayimg = cv.medianBlur(grayimg, 3)
maskimg = cv.adaptiveThreshold(grayimg, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 3)
maskimg = cv.cvtColor(maskimg, cv.COLOR_GRAY2BGR)
img = cv.bitwise_and(img,maskimg)

cv.imshow("Cartoonfilter", img)

cv.waitKey(0)
cv.destroyAllWindows()
