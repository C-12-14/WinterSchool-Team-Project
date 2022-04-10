import cv2
from cv2 import INTER_AREA
from maze_generation import createMaze
import sys
import time

sys.setrecursionlimit(1000000)
RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
COLOR1 = ()
COLOR2 = (61, 217, 255)
path_found = False
dist = 0
def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

def dfs2(inimg, start, end):
    img = inimg
    global path_found
    global dist
    i, j = start
    if img.shape[0] < 100:
        showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
        cv2.imshow("dfs", showImg)
        cv2.waitKey(1)
    else:
        cv2.imshow("dfs", img)
    for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:        # Loops over the surrounding pixels
        if inRange(img, (x+i, y+j)) and (img[x+i][y+j]!=BLACK).any() and (img[x+i][y+j]!=COLOR2).any():     # Check if pixel lies in the valid path
            if ((x+i, y+j) == end):       
                path_found = True
                img[i][j] = GREEN
                dist +=1
                break
            if (img[x+i][y+j] == WHITE).all():
                        img[x+i][y+j] = COLOR2
                        dfs2(img, (x+i,y+j), end)
            if path_found:      # Stops further recursion and starts traceback
                img[i][j] = GREEN
                if img.shape[0] < 100:
                    showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
                    cv2.imshow("dfs", showImg)
                    cv2.waitKey(1)
                else:
                    cv2.imshow("dfs", img)
                dist +=1
                break
 
def dfs(inimg, start, end):
    img = inimg
    dfs2(img, start,end)
    print("Distance: "+str(dist) + " pixels")

# start = time.time()
 
# end = time.time()
# print("Time: "+str(round(end-start, 4)) + " seconds")
# cv2.waitKey(0)
# cv2.destroyAllWindows()