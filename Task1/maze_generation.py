import cv2
from cv2 import INTER_AREA
import numpy as np
import random 

RED = (0,0,255)
BLUE = (255,0,0)
maze = []
prob = random.randint(20,30)

def createMaze():
    canvas = np.full((50, 50,3), 255, dtype=np.uint8)
    # canvas = np.full((50, 50,3), 255, dtype=np.uint8)
    for i in range(canvas.shape[0]):
        for j in range(canvas.shape[1]):
            randomnumber = random.randint(1, 100)
            if randomnumber<prob:
                canvas[i][j] = (0,0,0)
            else:
                maze.append((i,j))

    startXY = random.choice(maze)
    endXY  = random.choice(maze)

    canvas[startXY] = RED
    canvas[endXY] = BLUE
    smaller_canvas = canvas
    canvas = cv2.resize(canvas,(500,500), interpolation=cv2.INTER_AREA)

    return canvas, startXY, endXY, smaller_canvas
