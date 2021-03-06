import cv2
import time
import numpy as np
from maze_generation import createMaze
from Traversal_mod import MazeTraversal


# <---------- Variables to document time taken and distance ---------->
avg_time_Bfs = 0
avg_time_Dfs = 0
avg_time_Dijkstra = 0
avg_time_Astar = 0
avg_dist_Bfs = 0
avg_dist_Dfs = 0
avg_dist_Dijkstra = 0
avg_dist_Astar = 0

n = 1000  # number of iterations

for i in range(n):
    # print(i + 1, end="\t")
    # if (i + 1) % 10 == 0:
    #     print()
    maze, startXY, endXY, smaller_maze = createMaze()
    algos = MazeTraversal(smaller_maze, startXY, endXY)

    start = time.time()
    avg_dist_Bfs += algos.trackBfs() / n
    end = time.time()
    avg_time_Bfs += (end - start) / n

    start = time.time()
    avg_dist_Dfs += algos.dfs() / n
    end = time.time()
    avg_time_Dfs += (end - start) / n

    start = time.time()
    avg_dist_Dijkstra += algos.trackDijkstra() / n
    end = time.time()
    avg_time_Dijkstra += (end - start) / n

    start = time.time()
    avg_dist_Astar += algos.trackaStar() / n
    end = time.time()
    avg_time_Astar += (end - start) / n


print("Average time taken by BFS: " + str(avg_time_Bfs) + " Seconds")
print("Average distance travelled in BFS: " + str(avg_dist_Bfs) + " pixels")
print("----------------------------------------------------------")

print("Average time taken by DFS: " + str(avg_time_Dfs) + " Seconds")
print("Average distance travelled in DFS: " + str(avg_dist_Dfs) + " pixels")
print("----------------------------------------------------------")

print("Average time taken by Dijkstra: " + str(avg_time_Dijkstra) + " Seconds")
print("Average distance travelled in Dijkstra: " + str(avg_dist_Dijkstra) + " pixels")
print("----------------------------------------------------------")

print("Average time taken by Astar: " + str(avg_time_Astar) + " Seconds")
print("Average distance travelled in Astar: " + str(avg_dist_Astar) + " pixels")
print("----------------------------------------------------------")
