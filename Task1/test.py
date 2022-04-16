import cv2
maze = cv2.imread("Task1/processedmaze.png")
n, l = maze.shape[:2]
maze = cv2.resize(maze,(int(l*0.5), int(n*0.5)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("wefw", maze)
cv2.waitKey(0)