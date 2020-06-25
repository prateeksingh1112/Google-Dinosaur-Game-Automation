import pyautogui
from PIL import Image,ImageGrab

import time
    
from numpy import asarray
def hit(key):
    pyautogui.keyDown(key)
    return
#     image = ImageGrab.grab().convert("L")
# def ss():
#     return image


def isCollide(self):
    for i in range(210, 230):
        for j in range(380, 460):
            if data[i, j] < 100:
                 hit("up")
                 return
                 
    for i in range(250, 280):
        for j in range(320, 350):
            if data[i, j] < 171:    
                hit("down")
                return
    return 

if __name__=="__main__":
    time.sleep(2)
    hit("up")
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isCollide(data)
            
    # image = ImageGrab.grab().convert("L")
    # data = image.load()        
    # # print(asarray(image))
    # for i in range(250, 280):
    #     for j in range(320, 350):
    #         data[i, j] = 0
    # for i in range(210, 230):
    #     for j in range(380, 460):
    #         data[i, j] = 0        
    
    # image.show()
    
