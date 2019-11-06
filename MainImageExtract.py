from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageExtract:
    x_list = []
    y_list = []
    #size = None
    def __init__(self, image):
        self.image=image
        self.size = image.shape
        
        #for x in np.arange(0, size[1], 1):
         #   for y in np.arange(0,size[0], 1):
          #      if np.all(image[y][x] <= (180, 180,180)):
           #         self.x_list.append(x)
            #        self.y_list.append(size[0]-y)
    
    def start(self):
        for x in np.arange(0, self.size[1], 1):
            for y in np.arange(0,self.size[0], 1):
                if np.all(self.image[y][x] <= (180, 180,180)):
                    self.x_list.append(x)
                    self.y_list.append(self.size[0]-y) 

    def plotImage(self,show=False ,width=15, height=15):
        plt.figure(figsize = [width, height]) 
        plt.scatter(self.x_list, self.y_list, marker='.', s=3)
        if(show):
            plt.show()

#Test
image = cv2.imread('syncope-atrial-fib-w-slow-resp.png',1)
image_extract = ImageExtract(image)
image_extract.plotImage()






