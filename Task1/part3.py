import cv2
import time
import numpy as np
from Traversal import MazeTraversal

startXY = (335,139)
endXY = (226,720)
maze = cv2.imread("Task1/processedmaze.png")

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