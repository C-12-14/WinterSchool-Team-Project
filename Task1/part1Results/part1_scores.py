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

n=1000 #number of iterations

for i in range (n):
    maze,startXY,endXY, smaller_maze = createMaze()
    algos = MazeTraversal(smaller_maze, startXY, endXY)

    start = time.time()
    avg_dist_Bfs+=algos.trackBfs()
    end = time.time()
    avg_time_Bfs += (end-start)

    temp = np.copy(smaller_maze)
    algos = MazeTraversal(temp, startXY, endXY)
    start = time.time()
    avg_dist_Dfs+=algos.dfs()
    end = time.time()
    avg_time_Dfs += (end-start)

    temp = np.copy(smaller_maze)
    algos = MazeTraversal(temp, startXY, endXY)
    start = time.time()
    avg_dist_Dijkstra += algos.trackDijkstra()
    end = time.time()
    avg_time_Dijkstra += (end-start)

    temp = np.copy(smaller_maze)
    algos = MazeTraversal(temp, startXY, endXY)
    start = time.time()
    avg_dist_Astar += algos.trackaStar()
    end = time.time()
    avg_time_Astar += (end-start)


avg_time_Bfs /= n
avg_time_Dfs /= n
avg_time_Dijkstra /= n
avg_time_Astar /= n
avg_dist_Bfs /= n
avg_dist_Dfs /= n
avg_dist_Dijkstra /= n
avg_dist_Astar /= n

print("Average time taken by BFS: "+str(avg_time_Bfs) + " Seconds")
print("Average distance travelled in BFS: "+str(avg_dist_Bfs)+" pixels")
print("----------------------------------------------------------")

print("Average time taken by DFS: "+str(avg_time_Dfs)+ " Seconds")
print("Average distance travelled in DFS: "+str(avg_dist_Dfs)+" pixels")
print("----------------------------------------------------------")

print("Average time taken by Dijkstra: "+str(avg_time_Dijkstra)+ " Seconds")
print("Average distance travelled in Dijkstra: "+str(avg_dist_Dijkstra)+" pixels")
print("----------------------------------------------------------")

print("Average time taken by Astar: "+str(avg_time_Astar)+ " Seconds")
print("Average distance travelled in Astar: "+str(avg_dist_Astar)+" pixels")
print("----------------------------------------------------------")
