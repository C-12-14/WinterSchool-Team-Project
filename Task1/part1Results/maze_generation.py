import cv2
from cv2 import INTER_AREA
import numpy as np
import random
from Traversal_mod import MazeTraversal

RED = (0, 0, 255)
BLUE = (255, 0, 0)
maze = []  # For keeping track of valid path (White pixels)
prob = random.randint(20, 30)
startXY = ()
endXY = ()


def createMaze():
    canvas = np.full((30, 30, 3), 255, dtype=np.uint8)
    for i in range(canvas.shape[0]):
        for j in range(canvas.shape[1]):
            randomnumber = random.randint(1, 100)
            if randomnumber < prob:
                canvas[i][j] = (0, 0, 0)
            else:
                maze.append((i, j))  # Adding the pixel into valid path

    while True:
        global startXY, endXY
        startXY = random.choice(
            maze
        )  # Choosing a start location in the list of white pixels
        endXY = random.choice(
            maze
        )  # Choosing a end location in the list of white pixels
        temp = canvas.copy()
        if startXY != endXY:
            algos = MazeTraversal(temp, startXY, endXY)
            a, b = algos.aStar(temp)
            if a is not None:
                break

    canvas[startXY] = RED
    canvas[endXY] = BLUE
    smaller_canvas = canvas
    canvas = cv2.resize(canvas, (500, 500), interpolation=cv2.INTER_AREA)

    return canvas, startXY, endXY, smaller_canvas
