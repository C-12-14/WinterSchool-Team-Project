import cv2
import numpy as np
import time 
from maze_generation import createMaze

start = time.time()

RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

def find_dist(point, current):
    return (point[0] - current[0])**2 + (point[1] - current[1])**2
    #Since we dont need the exact distance, we will keep it as square itself

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])

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
                if inRange(img,point) and visited[point]==0 and not(img[point]==BLACK).all():
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

def show_path(img, start, end, shortest_path):
    img1 = img
    for coord in shortest_path:
            img1[coord] = GREEN
    img1[start] = RED
    img1[end] = BLUE
    return img1

maze,startXY,endXY, smaller_maze = createMaze()
path_dj = dijkstra(maze, startXY, endXY)
end = time.time()
path_dj_img = show_path(maze,startXY, endXY, path_dj)

cv2.imshow('Maze',maze)
cv2.imshow('Dijkstra Path',path_dj_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

time_taken = end - start
print(f"Time taken for dijkstra's algorithm: {time_taken} seconds")