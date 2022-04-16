import cv2
from cv2 import INTER_AREA
import numpy as np

RED = (0,0,255)
GREEN = (0,255,0)

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

colors = [[118,86,73], [68,227,239], [37,117,236], [244,243,241], [255,255,255],[128,98,86]]
maze = cv2.imread("Task1/googlemaps.png")
n, l = maze.shape[:2]
tempmaze = maze.copy()
for i in range(n):
    for j in range(l):
        iscolor = False
        for color in colors:
            if (maze[i][j] == color).all():
                tempmaze[i][j] = [255, 255, 255]
                for (r,s) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if inRange(maze, (r+i, s+j)):
                        tempmaze[r+i][s+j] =  [255, 255, 255]
                break
        if not iscolor: tempmaze[i][j] = [0,0,0]


tempmaze = cv2.resize(tempmaze,(int(l*0.5), int(n*0.5)), interpolation=INTER_AREA)
n, l = tempmaze.shape[:2]
for i in range(n):
    for j in range(l):
        if tempmaze[i][j][0] > 127:
             tempmaze[i][j] = (255,255,255)
        else:
            tempmaze[i][j] = (0,0,0)
startXY = (335,139)
endXY = (226,720)
tempmaze[startXY]=RED
tempmaze[endXY]=GREEN

cv2.imshow("mze", tempmaze)
cv2.waitKey(0)