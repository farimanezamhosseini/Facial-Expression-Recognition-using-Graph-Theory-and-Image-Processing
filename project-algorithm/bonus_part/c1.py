import cv2
from numpy import imag

emotions=['sad','happy','angry','neutral']

for emotion in emotions:

  with open(emotion+'.txt','r') as f:
    img = [line.strip() for line in f]
   
  for image in img:
    loadedImage = cv2.imread("images/"+image)
    cv2.imwrite("dataset/"+emotion+"/"+image,loadedImage)
print("done writing")