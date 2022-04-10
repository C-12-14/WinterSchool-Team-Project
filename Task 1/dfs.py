import cv2
from cv2 import INTER_AREA
from maze_generation import createMaze
import sys

sys.setrecursionlimit(2500)
RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
COLOR1 = ()
COLOR2 = (61, 217, 255)
path_found = False

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

def dfs2(img, start):
    global path_found
    i, j = start
    showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
    cv2.imshow("dfs2", showImg)
    cv2.waitKey(1)
    for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:        # Loops over the surrounding pixels
        if inRange(img, (x+i, y+j)) and (img[x+i][y+j]!=BLACK).any() and (img[x+i][y+j]!=COLOR2).any():     # Check if pixel lies in the valid path
            if (img[x+i][y+j] == BLUE).all():       # BLUE is the color of the target
                path_found = True
                img[i][j] = GREEN
                break
            if (img[x+i][y+j] == WHITE).all():
                        img[x+i][y+j] = COLOR2
                        dfs2(img, (x+i,y+j))
            if path_found:      # Stops further recursion and starts traceback
                img[i][j] = GREEN
                showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
                cv2.imshow("dfs2", showImg)
                cv2.waitKey(1)
                break

maze,startXY,endXY, smaller_maze = createMaze()
dfs2(smaller_maze, startXY)
cv2.waitKey(0)
cv2.destroyAllWindows()