from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from MainImageExtract import ImageExtract
import os
#import pickle


class UnitTest:
    def __init__(self, test_path):
        self.images_list = list()
        for file in os.listdir(test_path):
            file_path = os.path.join(test_path, file)
            try:
                image = cv2.imread(file_path,1)
                image_vec = ImageExtract(image)
                self.images_list.append(image_vec)
            except:
                print("could'nt read the image: " + str(file_path))

    def test_execute(self):
        for image in self.images_list:
            image.start()

    def plot_test_results(self):
        for image in self.images_list:
            image.plotImage()
            plt.show()
    
    def dump_test_data(self, path_out):
        with open(path_out, "wb") as f:
            pickle.dump(self.images_list, f)
            f.close()



#Test
path = r'C:\\Users\\nitza\\Documents\\ECG_images'
unit_test = UnitTest(path)
unit_test.test_execute()
unit_test.plot_test_results()
#path_to_dump = os.path.join(path, "dump_file.pkl")
#path_to_dump = "dump_file.pkl"
#unit_test.dump_test_data(path_to_dump) 


