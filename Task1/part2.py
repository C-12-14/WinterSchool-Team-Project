import cv2
import time
import numpy as np
from Traversal import MazeTraversal

RED = (0,0,255)
GREEN = (0,255,0)

maze = cv2.imread("Task1/imgpart2.png")
n, l = maze.shape[:2]
startXY = (145,880)
endXY = (563,359)
maze[startXY]=RED
maze[endXY]=GREEN

algos = MazeTraversal(maze, startXY, endXY)

temp = np.copy(maze)
print("BFS: ")
start = time.time()
algos.trackBfs()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(maze)
print("DFS: ")
start = time.time()
algos.dfs()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(maze)
print("Dijkstra: ")
start = time.time()
algos.dijkstra()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(maze)
print("A*: ")
start = time.time()
algos.trackaStar()
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

cv2.destroyAllWindows()