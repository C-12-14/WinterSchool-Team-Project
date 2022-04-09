import cv2
import numpy as np
import random 
"""
This task comprises three parts:
1. In the first part, using the probability of 0.2~0.3, you have to generate a maze. The maze will be such that each 
pixel or group of pixels in the image will either be a black pixel or a white pixel. Now, for this, initially, 
make the image of a small size and then resize it to the required size so that instead of getting a pixelated image, 
we will get chunks of black pixels. Also, take care to mark two points on the maze with a grey-coloured pixel, 
one of which will be the starting point and the other will be the ending point. The black pixel is synonymous with 
an obstacle, and the white pixel is synonymous with an open path. 
#!After completing the maze generation, the task is
#!  to start at one of the grey points and traverse through the maze to the other grey point. This should be done using a 
#!  variety of Path-finding Algorithms(A*, BFS, DFS, Dijkstra should be compulsorily used while using more path-finding 
#!  Graph/Tree Algorithms will fetch more points). Finally, document the time taken for path-finding and the distance of 
#!  path found for all the Algorithms for a variety of Randomly-generated images.
2. In the second part, there is a map provided to you(Attached in mail). The map has been pre-processed for you. 
It has a red pixel at (880, 145) and a green pixel at (359, 563). The red pixel is the start point, and the green 
pixel is the endpoint. You have to work on this map and get the shortest path from the start to the endpoint using 
the algorithms used in the first part of Task-1.
3. The third part is pretty straightforward. You have to get images of your locality from Google Maps. 
Set a start point and an endpoint manually and apply the algorithms after doing the required pre-processing.
"""

RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
maze = []
prob = random.randint(20,30)

def createMaze():
    canvas = np.full((50, 50,3), 255, dtype=np.uint8)
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

    canvas = cv2.resize(canvas,(500,500), interpolation=cv2.INTER_AREA)

    return canvas, startXY, endXY


def find_dist(point, current):
    return (point[0] - current[0])**2 + (point[1] - current[1])**2
    #Since we dont need the exact distance, we will keep it as square itself

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

def bfs():
    pass

def dfs():
    pass

def dijkstra(img, start, end):
    n,m,l = img.shape
    dist = np.full((n,m),fill_value = np.inf) #Stores distances of each pixel from start
    dist[start] = 0 
    parent = np.zeros((n,m,2)) #Stores x and y coordinates of parent, hence it has 3 dimensions
    visited = np.zeros((n,m)) #Stores whether a pixel has been visited or not
    visited[start] = 1
    current = start
    while current!=end:
        visited[current]=1 
        for i in range(-1,2): #-1,-0,1
            for j in range(-1,2): #-1,-0,1
                point = (current[0]+i,current[1]+j)
                if inRange(img,point) and visited[point]==0 and not(img[point][1]==BLACK[1] and img[point][2] == BLACK[2]):
                    if dist[point]>dist[current]+find_dist(point,current):
                        dist[point] = dist[current]+find_dist(point,current)
                        parent[point[0],point[1],0] = current[0]
                        parent[point[0],point[1],1] = current[1]

        #Finding the node with minimum distance, which will become the next node from which we check
        min = np.inf
        for i in range(n):
            for j in range(m):
                if dist[i,j] < min and visited[i,j] == 0:
                    min = dist[i,j]
                    current = (i,j)
        
    #now we will get the shortest path from the parent list
    curr_node = end
    shortest_path = []
    while curr_node!=start:
        shortest_path.append(curr_node)
        pair = int(parent[curr_node[0],curr_node[1],0]),int(parent[curr_node[0],curr_node[1],1])
        curr_node = (pair[0],pair[1])

    shortest_path.append(start)
    shortest_path.reverse()
    return shortest_path

def a_star():
    pass

def show_path(img, start, end, shortest_path):
    img1 = img
    for coord in shortest_path:
            img1[coord] = GREEN
    img1[start] = RED
    img1[end] = BLUE
    return img1

maze,startXY,endXY = createMaze()

path_dj = dijkstra(maze, startXY, endXY)
path_dj_img = show_path(maze,startXY, endXY, path_dj)


cv2.imshow("maze", maze)

cv2.imshow("path",path_dj_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
