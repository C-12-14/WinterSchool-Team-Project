import cv2
from cv2 import INTER_AREA
import numpy as np
import time

from maze_generation import createMaze

start = time.time()

RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
COLOR2 = (61, 217, 255)
def find_dist(point, current):
    return (point[0] - current[0])**2 + (point[1] - current[1])**2
    #Since we dont need the exact distance, we will keep it as square itself

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

def dijkstra(img, start, end):
    n, m = img.shape[:2]
    parent = np.zeros((n,m,2))
    visited = []
    current = start
    distance = np.full((n,m), np.inf)
    distance[start] = 0
    while True:
        if current != end:
            for (i, j) in [(-1,0), (1,0), (0,-1), (0,1)]:
                showImg = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
                cv2.imshow("dijkstra", showImg)
                cv2.waitKey(1)
                newpoint = (current[0]+i, current[1]+j)
                
                if inRange(img, newpoint) and not (img[newpoint] == BLACK).all():
                    if distance[newpoint] > distance[current] + find_dist(newpoint, current):
                        distance[newpoint] = distance[current] + find_dist(newpoint, current)
                        img[newpoint] = COLOR2
                        parent[newpoint] =  current
                        visited.append(newpoint)
                min = np.inf
            for point in visited:
                if distance[point] < min:
                    min = distance[point]
                    current = point
            visited.remove(current)
        else:
            img[end] = BLUE
            distance[end] = distance[current] +find_dist(end, current)
            return distance[end], parent

def trackDijkastra(img, start, end):
    dist, parent = dijkstra(img, start, end)
    current = tuple(list(map(int, parent[end])))
    while current != start:
        img[current] = GREEN
        current = tuple(list(map(int, parent[current])))
        showImg = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)
        cv2.imshow("dijkstra", showImg)
        cv2.waitKey(1)
    print("Distance: " + str(dist) + " pixels")

start = time.time()
maze,startXY,endXY, smaller_maze = createMaze()
trackDijkastra(smaller_maze, startXY, endXY)
end = time.time()
print(str(start-end) + " seconds")
cv2.waitKey(0)
# cv2.imshow('Maze',maze)
# cv2.imshow('Dijkstra Path',path_dj_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()