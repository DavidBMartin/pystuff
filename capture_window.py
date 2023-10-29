#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:25:58 2023
DRAG and RESIZE window returning geometry when escape is pressed
@author: srilthe
"""

from tkinter import Tk
import numpy as np
from PIL import ImageGrab
import cv2
import os

class new_window(): 
    def __init__(self, ar):
        self.w = ar[2]
        self.h = ar[3]
        self.x = ar[0]
        self.y = ar[1]
        window = Tk()        
        window.title("Capture")
        window.geometry(f'{self.w}x{self.h}+{self.x}+{self.y}')
        window.wait_visibility(window)
        window.wm_attributes('-alpha',0.55)
            
        def key_handler(event):
            if ord(event.char)  == 27:
                g = window.geometry()
                p = g.find('+')
                self.w, self.h, self.x, self.y = g[:p].split('x')+g[p+1:].split('+')
                window.destroy()
        
        window.bind("<Key>", key_handler)
        window.mainloop()
            
    def getBox(self):
        return([int(i) for i in (self.x, self.y, self.w, self.h)])    
    
    def getImage(cap):
        x, y, w, h = [int(i) for i in cap]
        bbox = (x, y, w+x, h+y+50)
        img = ImageGrab.grab(bbox)
        pil_image = img.convert('RGB') 
        open_cv_image = np.array(pil_image) 
        open_cv_image2 = open_cv_image[:, :, ::-1].copy() 
        return(open_cv_image2)
    
    def showImage(x, y, w, h):
        imName = f"{x},{y} {w},{h}"
        value = 0
        while True:
            key = cv2.waitKey(30)
            """if cv2.getWindowProperty(imName,cv2.WND_PROP_VISIBLE) < 1:
                break    """   
            if (key == ord('q')):  
                break
            try:
                img = new_window.getImage(x, y, w, h)
                val = sum(img.ravel())
                if val != value:
                    print(f"Changed {val}")
                    value = val                
                cv2.imshow(imName, img)
            except Exception as e:
                print(f"error: {e}")
        cv2.destroyAllWindows()

       
    def saveImage(x, y, w, h):
        imgPath = (f"{os.getcwd()}/img/")
        if not os.path.exists(imgPath):
            os.makedirs(imgPath)
        ctr = 0
        filename = f"{imgPath}A-{x},{y},{w},{h}-{ctr}.png" 
        while os.path.isfile(filename):
            ctr += 1
            filename = f"{imgPath}A-{x},{y},{w},{h}-{ctr}.png" 
        cv2.imwrite(filename, new_window.getImage(x, y, w, h))
        print(filename)
    
    

if __name__ == "__main__":
    """
    Only run directly for testing.
    """
    x, y, w, h = '629 867 124 32'.split(' ')
    ar = new_window(x, y, w, h)    
    #print('x, y, w, h', x, y, w, h)
    x, y, w, h = [int(i) for i in (ar.x, ar.y, ar.w, ar.h)]
    print(x, y, w, h)
    """#print('conv x, y, w, h', x, y, w, h)
    new_window.showImage(x, y, w, h)
    new_window.saveImage(x, y, w, h)"""

    
    
