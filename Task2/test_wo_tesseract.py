import cv2 
import numpy as np

def get_dominant_color(image):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags, labels, centres = cv2.kmeans(
        pixels, 1, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    return centres[0].astype(np.int32)

def get_turn(image):
    #!Template matching
    pass

def get_speed(image):
    #!Template matching
    pass

vid = cv2.VideoCapture('Task2\\task2_video.mp4')

while 1: 
    ret, frame = vid.read()
    cv2.imshow('camera', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)  
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1, 50, param1=120, param2=40)
    #getting relevant part of the image only using circle
    if circles is not None:
        circles = np.uint16(np.around(circles))
        max_r, max_i = 0, 0
        #To find the largest circle
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]
        else:
            square = frame[0:y+r, 0:x+r]

        #!for red, R>150, for green, G>150 
        #!for turns, G and R > 200
        #!for speed signs, all>150
        
        dominant_color = get_dominant_color(square)

        if dominant_color[2] > 150 and not (dominant_color[1] > 150 and dominant_color[0] > 150):
            #it's a stop sign
            print("STOP")
        elif dominant_color[1] > 150 and not (dominant_color[2] > 150 and dominant_color[0] > 150):
            #it's a go sign
            print("GO")
        elif dominant_color[1] > 200 and dominant_color[2] > 200 and not (dominant_color[0] > 200):
            #it's a turn sign
            turn = get_turn(square)
            print(turn)
        elif all(dominant_color > 150):
            #it's a speed sign
            speed = get_speed(square)
            print(speed)

    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('0'): 
        break


vid.release()
cv2.destroyAllWindows()
