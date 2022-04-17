import cv2
from cv2 import INTER_AREA
import numpy as np
import random 

RED = (0,0,255)
BLUE = (255,0,0)
maze = []
prob = random.randint(20,30)

def inRange(canvas,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<canvas.shape[0] and point[1]>=0 and point[1]<canvas.shape[1])


def checkNbhd(canvas, x, y):
    #check if atleast more than one white neighbour is present
    count = 0
    for (i, j) in [(-1,0), (1,0), (0,-1), (0,1)]:
        if inRange(canvas, (x+i, y+j)) and (canvas[x+i][y+j] == (255,255,255)).all():
            count+=1
    if(count>1): 
        return True
    else:
        return False

def createMaze():
    canvas = np.full((50, 50, 3), 255, dtype=np.uint8)
    # canvas = np.full((50, 50,3), 255, dtype=np.uint8)
    for i in range(canvas.shape[0]):
        for j in range(canvas.shape[1]):
            randomnumber = random.randint(1, 100)
            if randomnumber<prob and checkNbhd(canvas,i,j):
                canvas[i][j] = (0,0,0)
            else:
                if checkNbhd(canvas,i,j):
                    maze.append((i,j))

    startXY = random.choice(maze)
    endXY  = random.choice(maze)
    while(endXY==startXY):
        endXY  = random.choice(maze)

    canvas[startXY] = RED
    canvas[endXY] = BLUE
    smaller_canvas = canvas
    canvas = cv2.resize(canvas,(500,500), interpolation=cv2.INTER_AREA)

    return canvas, startXY, endXY, smaller_canvas
