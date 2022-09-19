# -*- coding: utf-8 -*-
"""BrainTumor_DeployModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EgOjJmCGgkkhSL4dDEMoqmqEWF_iGVuO
"""

import keras
from keras.models import *
from keras.layers import *
from keras.preprocessing import image
import PIL
from google.colab import drive
drive.mount('/content/drive')
from keras.models import load_model
model=load_model("/content/drive/MyDrive/H5_Folders/BrainTumor_CNN.h5")

import cv2
from numpy import asarray
img =cv2.imread("/content/sample_data/yes2.jfif",0)
img

# importing cv2 
import numpy as np
img=cv2.resize(img, (100, 100)) 
img=np.array(img).astype(np.uint8)

img=image.img_to_array(img)
img.shape

img=img/255.0
img_expand=np.expand_dims(img,axis=0)#img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
img_expand.shape

y_pred_img=model.predict(img_expand)
print(y_pred_img)

if(y_pred_img >=0.5):
  print("Brain Tumor")
else:
  print("No Brain Tumor")