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
        self.label = tk.Label(self.root, text="Please choose the images you'd like to merge.").pack(side="bottom")
        self.width = 200;
        self.height = 200;
        self.count=1;
        self.faceSpace = np.empty([self.width, self.height, 3])
    def add(self):
        gi1 = cv2.imread(askopenfilename());
        gi1 = cv2.cvtColor(gi1, cv2.COLOR_BGR2GRAY)
        face1 = detector.detectMultiScale(gi1);            
        if len(face1) == 0:
            raise "No Faces Have been Found."
        
        print(f" Number of faces found were : {len(face1)} ")
        (x1, y1, X1, Y1) = face1[0];
        print(f"x1,y1,X1,Y1 : {x1,y1,X1,Y1}" )
        gi1 = gi1[y1:X1+Y1]
        #gi2 = gi2[x2+y2:X2-Y2]
    
        try:
            gi1 = cv2.resize(gi1, (self.width, self.height), 3);
        except Exception as e:
            print(" This image is invalid, choose another one."); return;
    
        imgArray = np.resize(np.array(gi1), (self.width, self.height, 3));
        self.count += 1;
        self.faceSpace = (self.faceSpace + imgArray)/self.count
        
    def Merge(self):
      
        
        fileName = time.strftime("%Y_%m_%d_%H_%M_%S")
        cv2.imwrite('img' + fileName + '.png', self.faceSpace)
        self.faceSpace = np.empty([self.width, self.height, 3])
        self.count=1;
        cv2.imshow("That's an Image.", cv2.imread(f"img{fileName}.png"));



if __name__ == '__main__':
    print("Please Wait.. ")
    obj = Averager()

        
