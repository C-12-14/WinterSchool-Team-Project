import cv2
<<<<<<< HEAD
import numpy as np
=======
import time
import numpy as np
from bfs import trackBfs
from dfs import dfs
from dijkstra2 import trackDijkastra as dijkstra
from a_star import trackaStar as astar

startXY = (335,139)
endXY = (226,720)
maze = cv2.imread("Task1/processedmaze.png")

temp = np.copy(maze)
print("BFS: ")
start = time.time()
trackBfs(temp, startXY, endXY)
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(maze)
print("DFS: ")
start = time.time()
dfs(temp, startXY, endXY)
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(maze)
print("Dijkstra: ")
start = time.time()
dijkstra(temp, startXY, endXY)
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

temp = np.copy(maze)
print("A*: ")
start = time.time()
astar(temp, startXY, endXY)
end = time.time()
print("Time: "+str(round(end-start, 4)) + " seconds")
print("------------------------------------------------")
cv2.waitKey(0)

cv2.destroyAllWindows()
>>>>>>> upstream/main
