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
           'Keep right',     
           'Keep left',      
           'Roundabout mandatory',     
           'End of no passing',      
           'End no passing veh > 3.5 tons')


model = load_model('traffic_classifier.h5')

cap = cv.VideoCapture('Task2/video.mp4')

while True:
    success, frame = cap.read()

    image = Image.fromarray(frame)
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = model.predict([image]).argmax()
    sign = classes[pred]
    print(sign)

    if not success:
        break

    cv.imshow('Output', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
