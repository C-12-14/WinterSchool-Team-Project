import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def get_square(image):
    #gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(image, 37)  
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT,1, 50, param1=120, param2=40)    
    circles = np.uint16(np.around(circles))
    max_r, max_i = 0, 0
    #To find the largest circle
    for i in range(len(circles[:, :, 2][0])):
        if circles[:, :, 2][0][i] > max_r:
            max_i = i
            max_r = circles[:, :, 2][0][i]
    x, y, r = circles[:, :, :][0][max_i]
    if y > r and x > r:
        square = image[y-r:y+r, x-r:x+r]
    else:
        square = image[0:y+r, 0:x+r]
    return square

def template_match(image,template,method):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    res = cv.matchTemplate(img_gray, template_gray, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(f"Image shape is {w},{h}")
    print(f"Max and min locations are {max_loc},{min_loc}")
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(image, top_left, bottom_right, 255, 2)
    return image

l_img = cv.imread('Signs/turnleft.jpeg')
l_template = cv.imread('templates/leftt.png')
r_img = cv.imread('Signs/turnright.png')
r_template = cv.imread('templates/rightt.png')
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    cv.imshow('image',template_match(l_img,l_template,method=eval(meth)))
    cv.imshow('image',template_match(r_img,r_template,method=eval(meth)))
    cv.imshow('image',template_match(l_img,r_template,method=eval(meth)))
    cv.waitKey(0)
    cv.destroyAllWindows()