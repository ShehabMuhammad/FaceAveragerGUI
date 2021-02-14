import tkinter as tk
from tkinter.filedialog import askopenfilename
import os, time, cv2
from PIL import Image
import numpy as np


detector = cv2.CascadeClassifier("detector.xml");

class Averager():
    def __init__(self):
        self.root = tk.Tk();
        self.button1 = tk.Button(self.root, text="save the image.", command=self.Merge).pack()
        self.button2 = tk.Button(self.root, text="Add a face.", command=self.add).pack()
        self.label = tk.Label(self.root, text="Please choose two frontal face images, With no swayings").pack(side="bottom")
        self.width = 200;
        self.height = 200;
        self.faceSpace = np.empty([self.width, self.height, 3])
    def add(self, face):
        gi1 = cv2.imread(askopenfilename());

        gi1 = cv2.cvtColor(gi1, cv2.COLOR_BGR2GRAY)

        face1 = detector.detectMultiScale(gi1, 1.1, 5);
        if len(face1) == 0 or len(face2) == 0:
            raise "No Faces Have been Found."
        
        #print(f" Number of faces found were : {len(face1)} and {len(face2)}")
        (x1, y1, X1, Y1) = face1[0];
        #gi1 = gi1[x1+y1:X1-Y1]
        #gi2 = gi2[x2+y2:X2-Y2]            
        gi1 = cv2.resize(gi1, (self.width, self.height), 3);
    
        imgArray = np.resize(np.array(gi1), (self.width, self.height, 3));
        self.faceSpace = (self.faceSpace + imgArray)/2
        
    def Merge(self):
      
        
        fileName = time.strftime("%Y_%m_%d_%H_%M_%S")
        
        cv2.imwrite('img' + fileName + '.png', self.faceSpace)
        
        cv2.imshow("That's an Image.", cv2.imread(f"img{fileName}.png"));



if __name__ == '__main__':
    obj = Averager()

        
