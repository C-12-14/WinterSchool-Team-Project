import cv2
import numpy as np 

"""
This task comprises two main parts and one bonus part:
1. In the first part, you have to generate a 1-2 minute long video using
12-15 (can be more depending on you) images. These images will be of traffic lights
(it will be two images, with green light and red light), Stop signals, speed signals(2-3 different speeds), 
turn signals, etc. The mentioned ones are compulsory to use in generating the video. Along with it, use more 
images to complete the 12-15 images requirement.
2. In the second part, the video generated in the first part will be run and depending on the different road signals, 
the program will generate different outputs and store them in a text file. For example, let’s say the output stores
 the speeds of the left and right motors, so upon showing the green signal, both the motors will keep running. If a 
 red sign pops up, the motors will stop unless and until a new image of the green sign comes up. Some things have to
  be taken care of, like, if a red sign has come up, or a Stop signal has come up, then immediately after it, a green 
  sign should come, or a Go signal should come.
3. This is the bonus part. It comprises three parts:
a. The first part of the bonus task is a parallel implementation of
video generation and storing the output in the text file.
b. The second part is the hardware implementation of the whole
thing. This means that the output produced in the text file should be read and sent to the Arduino, 
where it will drive the motors depending on the output coming to it.
c. In the third part, implement everything in sync i.e. in parallel.
"""