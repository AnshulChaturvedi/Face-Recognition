import os
import cv2
from PIL import Image 
import numpy as np

def train_classifier(data_dir):
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    
    faces = []
    ids = []
    
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        
        faces.append(imageNp)
        ids.append(id)
        
    ids = np.array(ids)
    
    
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("C:/Users/Shresth Jalan/Downloads/p1frs/p1/backen/classifier.xml")
train_classifier("C:/Users/Shresth Jalan/Downloads/p1frs/p1/backen/data")