from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv
from PIL import Image

classes = ('20','30','50','60','70','80',     
            'End of speed limit (80km/h)',     
            '100','120',     
           'No passing',   
           'No passing veh over 3.5 tons',     
           'Right-of-way at intersection',     
           'Priority road',    
           'Yield',     
           'Stop',       
           'No vehicles',       
           'Veh > 3.5 tons prohibited',       
           'No entry',       
           'General caution',     
           'Dangerous curve left',      
           'Dangerous curve right',   
           'Double curve',      
           'Bumpy road',     
           'Slippery road',       
           'Road narrows on the right',  
           'Road work',    
           'Traffic signals',      
           'Pedestrians',     
           'Children crossing',     
           'Turn left ahead',       
           'Beware of ice/snow',
           'Wild animals crossing',      
           'End speed + passing limits',      
           'Turn right ahead',     
           'Bicycle Crossing',       
           'Ahead only',      
           'Go straight or right',      
           'Go straight or left',      
           'Red Traffic Light',     
           'Keep left',      
           'Green Traffic Light',     
           'End of no passing',      
           'End no passing veh > 3.5 tons')
model = load_model('Task2/traffic_classifier.h5')
cap = cv.VideoCapture('Task2/video.mp4')
sign = 0
diameter = 0.1524        # diameter = 6 inches or 15.24 cm

while True:
    with open("Task2/output.txt", "a") as myfile:
        success, frame = cap.read()
        if not success:
            break
        image = Image.fromarray(frame)
        image = image.resize((30, 30))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        pred = model.predict([image]).argmax()
        tempsign = classes[pred]
        if tempsign != sign:
            sign = tempsign
            if sign in ["Stop", "Red Traffic Light"]:
                myfile.write("Stop Motor\n")
                print(sign)
            elif sign == "Green Traffic Light":
                myfile.write("Start Motor\n")
                print(sign)
            elif sign in ['20','30','50','60','70','80','100','120'] :
                rpm = (50*int(sign))/(3*np.pi*diameter)             # calculating rpm from speed(km/hr)
                myfile.write("%.2f"%rpm)
                myfile.write("\n")
                print(sign + " km/hr")
            else:
                myfile.write(sign + "\n")
                print(sign)


        cv.imshow('Output', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
