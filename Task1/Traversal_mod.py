import cv2
import numpy as np
import sys


# <---------- Global variables definition ---------->
RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
COLOR1 = ()
COLOR2 = (61, 217, 255)
sys.setrecursionlimit(20000000)
path_found = False
dist = 0


# <---------------- COMMON FUNCTIONS ---------------->
def find_dist(point, current):
    return (point[0] - current[0])**2 + (point[1] - current[1])**2
    #Since we dont need the exact distance, we will keep it as square itself

def inRange(img,point):
    #checks if point is within the range of the image's dimensions
    return (point[0]>=0 and point[0]<img.shape[0] and point[1]>=0 and point[1]<img.shape[1])


class MazeTraversal:
    def __init__(self, inimg, start, end):
        self.inimg = inimg
        self.start = start
        self.end = end

    # <--------------------- BFS --------------------->
    def bfs(self, img):
        q = [[self.start]]       # QUeue for keeping track of path

        while q:
            # if img.shape[0] < 100:
            #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
            #     cv2.imshow("bfs", showImg)
            #     cv2.waitKey(1)
            # else:
            #     cv2.imshow("bfs", img)
            path = q.pop(0)         # Choosing a path from the queue
            r, s = path[-1]         # Coordinates of the last pixel in path

            for (u,v) in [(-1,0), (1,0), (0,-1), (0,1)]:        # Looping over the four corners of the pixel
                    if inRange(img, (r+u,s+v)) and (img[r+u][s+v]!=BLACK).any() and (img[r+u][s+v]!=COLOR2).any():
                        # if img.shape[0] < 100:
                        #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
                        #     cv2.imshow("bfs", showImg)
                        #     cv2.waitKey(1)
                        # else:
                        #     cv2.imshow("bfs", img)
                        if (img[r+u][s+v] == WHITE).all():
                            img[r+u][s+v] = COLOR2          # Coloring the visited pixel
                            new_path = list(path)           
                            new_path.append((r+u, s+v))     # Adding the visited pixel to it's parent path
                            q.append(new_path)              # updating the path in queue
                        elif ((r+u, s+v) == self.end):
                            return path                  # Returning the path from self.start to the self.end when the self.end is visited

    def trackBfs(self):
        img = np.copy(self.inimg)
        path= self.bfs(img)
        path.pop(0)
        for pixel in path:
            img[pixel] = GREEN
            # if img.shape[0] < 100:
            #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
            #     cv2.imshow("bfs", showImg)
            #     cv2.waitKey(1)
            # else:
            #     cv2.imshow("bfs", img)
        #print("Distance: "+str(len(path)+1) + " pixels")
        return len(path)+1


    # <--------------------- DFS --------------------->

    def dfs2(self, img, start):
        global path_found
        global dist
        i, j = start
        # if img.shape[0] < 100:
        #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
        #     cv2.imshow("dfs", showImg)
        #     cv2.waitKey(1)
        # else:
        #     cv2.imshow("dfs", img)
        for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:        # Loops over the surrounding pixels
            if inRange(img, (x+i, y+j)) and (img[x+i][y+j]!=BLACK).any() and (img[x+i][y+j]!=COLOR2).any():     # Check if pixel lies in the valid path
                if ((x+i, y+j) == self.end):       
                    path_found = True
                    img[i][j] = GREEN
                    dist +=1
                    break
                if not (img[x+i][y+j] == BLUE).all() and not (img[x+i][y+j] == RED).all():
                            img[x+i][y+j] = COLOR2
                            self.dfs2(img, (x+i,y+j))
                if path_found:      # Stops further recursion and starts traceback
                    img[i][j] = GREEN
                    # if img.shape[0] < 100:
                    #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
                    #     cv2.imshow("dfs", showImg)
                    #     cv2.waitKey(1)
                    # else:
                    #     cv2.imshow("dfs", img)
                    dist +=1
                    break
    
    def dfs(self):
        global path_found
        path_found = False
        img = np.copy(self.inimg)
        self.dfs2(img, self.start)
        #print("Distance: "+str(dist) + " pixels")
        return int(dist)


    # <--------------------- DIJKSTRA --------------------->

    def dijkstra(self, img):
        # img = np.copy(self.inimg)
        n, m = img.shape[:2]
        parent = np.zeros((n,m,2))
        visited = []
        current = self.start
        distance = np.full((n,m), np.inf)
        distance[self.start] = 0
        while True:
            if current != self.end:
                for (i, j) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    # if img.shape[0] < 100:
                    #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
                    #     cv2.imshow("dijkastra", showImg)
                    #     cv2.waitKey(1)
                    # else:
                    #     cv2.imshow("dijkastra", img)
                    newpoint = (current[0]+i, current[1]+j)
                    if inRange(img, newpoint) and not (img[newpoint] == BLACK).all():
                        if distance[newpoint] > distance[current] + find_dist(newpoint, current):
                            distance[newpoint] = distance[current] + find_dist(newpoint, current)
                            img[newpoint] = COLOR2
                            parent[newpoint] =  current
                            visited.append(newpoint)
                    min = np.inf
                for point in visited:
                    if distance[point] < min:
                        min = distance[point]
                        current = point
                visited.remove(current)
            else:
                img[self.end] = BLUE
                distance[self.end] = distance[current] +find_dist(self.end, current)
                return distance[self.end], parent

    def trackDijkastra(self):
        img = np.copy(self.inimg)
        dist, parent = self.dijkstra(img)
        current = tuple(list(map(int, parent[self.end])))
        while current != self.start:
            img[current] = GREEN
            current = tuple(list(map(int, parent[current])))
            # if img.shape[0] < 100:
            #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
            #     cv2.imshow("dijkastra", showImg)
            #     cv2.waitKey(1)
            # else:
            #     cv2.imshow("dijkastra", img)
        #print("Distance: " + str(int(dist)) + " pixels")
        return int(dist)


    # <--------------------- A* --------------------->
    def aStar(self, img):
        n, m = img.shape[:2]
        parent = np.zeros((n,m,2))
        visited = []
        current = self.start
        distance = np.full((n,m), np.inf)
        pixel_distance = np.full((n,m), np.inf)
        distance[self.start] = 0
        pixel_distance[self.start] = 0
        while True:
            if current != self.end:
                for (i, j) in [(-1,0), (1,0), (0,-1), (0,1)]:
                    # if img.shape[0] < 100:
                    #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
                    #     cv2.imshow("A*", showImg)
                    #     cv2.waitKey(1)
                    # else:
                    #     cv2.imshow("A*", img)
                    newpoint = (current[0]+i, current[1]+j)
                    if inRange(img, newpoint) and not (img[newpoint] == BLACK).all():
                        pixel_distance[newpoint] = pixel_distance[current] + find_dist(newpoint, current)
                        if distance[newpoint] > pixel_distance[newpoint]+ find_dist(newpoint, current) + find_dist(newpoint, self.end):
                            distance[newpoint] = pixel_distance[newpoint] + find_dist(newpoint, current)+ find_dist(newpoint, self.end)
                            img[newpoint] = COLOR2
                            parent[newpoint] =  current
                            visited.append(newpoint)
                    min = np.inf
                for point in visited:
                    if distance[point] < min:
                        min = distance[point]
                        current = point
                visited.remove(current)
            else:
                img[self.end] = BLUE
                distance[self.end] = distance[current] +find_dist(self.end, current)
                return distance[self.end], parent

    def trackaStar(self):
        img = np.copy(self.inimg)
        dist, parent = self.aStar(img)
        current = tuple(list(map(int, parent[self.end])))
        dist = 1
        while current != self.start:
            dist += 1
            img[current] = GREEN
            current = tuple(list(map(int, parent[current])))
            # if img.shape[0] < 100:
            #     showImg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
            #     cv2.imshow("A*", showImg)
            #     cv2.waitKey(1)
            # else:
            #     cv2.imshow("A*", img)
        #print("Distance: " + str(dist) + " pixels")
        return int(dist)
    
