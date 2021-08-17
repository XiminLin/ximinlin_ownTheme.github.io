import cv2
import numpy as np

img1 = "/Users/ximinlin/Downloads/Resume/00001.jpg"
img2 = "/Users/ximinlin/Downloads/Resume/00002.jpg"

img1 = cv2.imread(img1)
img2 = cv2.imread(img2)

height,width,_ = img1.shape

output_image = np.zeros((int(height * 1.25), width, 3), dtype='uint8')

output_image[:height, :width, :] = img1
output_image[height:, :width, :] = img2[:int(0.25*height)]

cv2.imshow("tmp", output_image)
k = cv2.waitKey(0)
