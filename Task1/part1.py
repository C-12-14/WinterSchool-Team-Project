import cv2
import time
import numpy as np
from maze_generation import createMaze
from Traversal import MazeTraversal


maze,startXY,endXY, smaller_maze = createMaze()

algos = MazeTraversal(smaller_maze, startXY, endXY)

"""
PRESS ANY KEY AFTER THE PATH FINDING IS COMPLETE TO GO THE THE NEXT ALGORITHM
"""

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
algos.trackDijkstra()
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
