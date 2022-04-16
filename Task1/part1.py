import cv2
import time
import numpy as np
from maze_generation import createMaze
from Traversal import MazeTraversal
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
"""

maze,startXY,endXY, smaller_maze = createMaze()

algos = MazeTraversal(maze, startXY, endXY)

"""
PRESS ANY KEY AFTER THE PATH FINDING IS COMPLETE TO GO THE THE NEXT ALGORITHM
"""

temp = np.copy(smaller_maze)
print("BFS: ")
start = time.time()
algos.trackBfs()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(smaller_maze)
print("DFS: ")
start = time.time()
algos.dfs()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(smaller_maze)
print("Dijkstra: ")
start = time.time()
algos.dijkstra()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(smaller_maze)
print("A*: ")
start = time.time()
algos.trackaStar()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

cv2.destroyAllWindows()
