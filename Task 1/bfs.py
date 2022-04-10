import cv2
from cv2 import INTER_AREA
from maze_generation import createMaze
import time

RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
COLOR1 = ()
COLOR2 = (61, 217, 255)

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

def bfs(inimg,start):
    img = inimg.copy()
    q = [[start]]       # QUeue for keeping track of path

    while q:
        showImg = cv2.resize(img, (500, 500), interpolation=INTER_AREA)         # Upscaling image for better view
        cv2.imshow("BFS",showImg)
        cv2.waitKey(1)
        path = q.pop(0)         # Choosing a path from the queue
        r, s = path[-1]         # Coordinates of the last pixel in path

        for (u,v) in [(-1,0), (1,0), (0,-1), (0,1)]:        # Looping over the four corners of the pixel
                if inRange(img, (r+u,s+v)) and (img[r+u][s+v]!=BLACK).any() and (img[r+u][s+v]!=COLOR2).any():
                    showImg = cv2.resize(img, (500, 500), interpolation=INTER_AREA)
                    cv2.imshow("BFS",showImg)
                    cv2.waitKey(1)
                    if (img[r+u][s+v] == WHITE).all():
                        img[r+u][s+v] = COLOR2          # Coloring the visited pixel
                        new_path = list(path)           
                        new_path.append((r+u, s+v))     # Adding the visited pixel to it's parent path
                        q.append(new_path)              # updating the path in queue
                    elif (img[r+u][s+v] ==  BLUE).all():
                        return path, img                     # Returning the path from start to the end when the end is visited

def trackBfs(inimg,start):
    img = inimg
    path, img = bfs(img,start)
    path.pop(0)
    showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
    for pixel in path:
        img[pixel] = GREEN
        showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
        cv2.imshow("BFS", showImg)
        cv2.waitKey(1)
    print("Distance: "+str(len(path)+1) + " pixels")

# start = time.time()
#  maze,startXY,endXY, smaller_maze = createMaze()
# trackBfs(smaller_maze, startXY)
# end = time.time()
# print("Time: "+str(round(end-start, 4)) + " seconds")
cv2.waitKey(0)
cv2.destroyAllWindows()