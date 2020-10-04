import tkinter as tk
from tkinter.filedialog import askopenfilename
import os, time, cv2
from PIL import Image
import numpy as np


detector = cv2.CascadeClassifier("detector.xml");

class Averager():
    def __init__(self):
        self.root = tk.Tk();
        self.button1 = tk.Button(self.root, text="Choose Two Images To Merge.", command=self.Merge).pack()
        self.label = tk.Label(self.root, text="Please choose two frontal face images, With no swayings").pack(side="bottom")
        self.width = 200;
        self.height = 200;
        self.faceSpace = np.empty([self.width, self.height, 3])

    def Merge(self):
        gi1 = cv2.imread(askopenfilename());
        gi2 = cv2.imread(askopenfilename());

        gi1 = cv2.cvtColor(gi1, cv2.COLOR_BGR2GRAY)
        gi2 = cv2.cvtColor(gi2, cv2.COLOR_BGR2GRAY);

        face1 = detector.detectMultiScale(gi1, 1.1, 5);
        face2 = detector.detectMultiScale(gi2, 1.1, 5);
        if len(face1) == 0 or len(face2) == 0:
            raise "No Faces Have been Found."
        
        #print(f" Number of faces found were : {len(face1)} and {len(face2)}")
        (x1, y1, X1, Y1) = face1[0];
        (x2, y2, X2, Y2) = face2[0];
        #gi1 = gi1[x1+y1:X1-Y1]
        #gi2 = gi2[x2+y2:X2-Y2]            
        gi1 = cv2.resize(gi1, (self.width, self.height), 3);
        gi2 = cv2.resize(gi2, (self.width, self.height), 3);
    
        imgArray = np.resize(np.array(gi1), (self.width, self.height, 3));
        img1Array = np.resize(np.array(gi2), (self.width, self.height, 3))
        
        faceSpace = self.faceSpace
        
        faceSpace = faceSpace + imgArray
        faceSpace = faceSpace + img1Array;
        
        faceSpace = faceSpace / 2;
        
        fileName = time.strftime("%Y_%m_%d_%H_%M_%S")
        
        cv2.imwrite('img' + fileName + '.png', faceSpace)
        
        cv2.imshow("That's an Image.", cv2.imread(f"img{fileName}.png"));



if __name__ == '__main__':
    obj = Averager()

        
