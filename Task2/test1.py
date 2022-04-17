import numpy as np
import cv2

def get_dominant_color(image,n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags, labels, centres = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    return centres[0].astype(np.int32)


def get_square(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)  
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, 50, param1=120, param2=40)    
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

def get_from_circle(image):
    square = get_square(image)
    dominant_color = get_dominant_color(square, 1)
    return dominant_color


turn1 = cv2.imread('turnright.png')
print(get_dominant_color(turn1, 1))

turn2 = cv2.imread('turnleft.jpeg')
print(get_dominant_color(turn2, 1))

turn3 = cv2.imread('turnU.png')
print(get_dominant_color(turn3, 1))


# red1 = cv2.imread('red1.jpeg')
# print(get_dominant_color(red1, 1))
# print(get_from_circle(red1))


# green1 = cv2.imread('green1.jpeg')
# print(get_dominant_color(green1, 1))
# print(get_from_circle(green1))



# speed = cv2.imread('speed.jpeg')
# print(get_dominant_color(speed, 1))
# print(get_from_circle(speed))
# square = get_square(speed)

# # dilation = cv2.dilate(thresh1, rect_kernel, iterations = 3)
# # contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# # im2 = square.copy()

# # for cnt in contours:
# #     x, y, w, h = cv2.boundingRect(cnt)
# #     # Draw the bounding box on the text area
# #     rect=cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
# #     # Crop the bounding box area
# #     cropped = im2[y:y + h, x:x + w]
# #     cv2.imwrite('rectanglebox.jpg',rect)
# #     # open the text file
# #     # Using tesseract on the cropped image area to get text
# #     text = pytesseract.image_to_string(cropped)
# #     print(text)

# speed1 = cv2.imread('speed1.jpeg')
# print(get_dominant_color(speed1, 1))
# print(get_from_circle(speed1))
# print(get_speed(get_square(speed)))


cv2.waitKey(0)
cv2.destroyAllWindows()
