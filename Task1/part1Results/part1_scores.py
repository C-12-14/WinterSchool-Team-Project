import cv2
import time
import numpy as np
from maze_generation import createMaze
from Traversal_mod import MazeTraversal


maze,startXY,endXY, smaller_maze = createMaze()

algos = MazeTraversal(smaller_maze, startXY, endXY)

# <---------- Variables to document time taken and distance ---------->
avg_time_Bfs = 0
avg_time_Dfs = 0
avg_time_Dijkstra = 0
avg_time_Astar = 0
avg_dist_Bfs = 0
avg_dist_Dfs = 0
avg_dist_Dijkstra = 0
avg_dist_Astar = 0


for i in range (1000):
    start = time.time()
    avg_dist_Bfs+=algos.trackBfs()
    end = time.time()
    avg_time_Bfs += (end-start)

    temp = np.copy(smaller_maze)
    start = time.time()
    avg_dist_Dfs+=algos.dfs()
    end = time.time()
    avg_time_Dfs += (end-start)

    temp = np.copy(smaller_maze)
    start = time.time()
    avg_dist_Dijkstra += algos.trackDijkastra()
    end = time.time()
    avg_time_Dijkstra += (end-start)

    temp = np.copy(smaller_maze)
    start = time.time()
    avg_dist_Astar += algos.trackaStar()
    end = time.time()
    avg_time_Astar += (end-start)


avg_time_Bfs /= 1000
avg_time_Dfs /= 1000
avg_time_Dijkstra /= 1000
avg_time_Astar /= 1000
avg_dist_Bfs /= 1000
avg_dist_Dfs /= 1000
avg_dist_Dijkstra /= 1000
avg_dist_Astar /= 1000

print("Average time taken by BFS: "+str(avg_time_Bfs))
print("Average distance travelled in BFS: "+str(avg_dist_Bfs)+" pixels")
print("------------------------------------------------")

print("Average time taken by DFS: "+str(avg_time_Dfs))
print("Average distance travelled in DFS: "+str(avg_dist_Dfs)+" pixels")
print("------------------------------------------------")

print("Average time taken by Dijkstra: "+str(avg_time_Dijkstra))
print("Average distance travelled in Dijkstra: "+str(avg_dist_Dijkstra)+" pixels")
print("------------------------------------------------")

print("Average time taken by Astar: "+str(avg_time_Astar))
print("Average distance travelled in Astar: "+str(avg_dist_Astar)+" pixels")
print("------------------------------------------------")
