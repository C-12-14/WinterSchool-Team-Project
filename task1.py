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

def bfs():
    pass

def dfs():
    pass

def dijkstra():
    pass

def a_star():
    pass

def show_path():
    pass

maze = np.full((50,50), 0)
prob = random.uniform(0.20,0.30) #! probability between 0.2 and 0.3

for i in range(50):
    for j in range(50):
        if random.random() < prob:
            maze[i][j] = 255


maze = cv2.resize(maze.astype(np.uint8),(600,600))

x1,y1 = random.randint(0,600),random.randint(0,600) #! Start point
x2,y2 = random.randint(0,600),random.randint(0,600) #! End point
maze[x1,y1] = maze [x2,y2] = 127
start = (x1,y1)
end = (x2,y2)

#! Black => Obstacle, White => Path

cv2.namedWindow('Maze',cv2.WINDOW_NORMAL)
cv2.imshow('Maze',maze.astype(np.uint8))


cv2.waitKey(0)
cv2.destroyAllWindows()