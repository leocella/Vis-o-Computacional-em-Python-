import cv2
import numpy as np 
from matplotlib import pyplot as plt

I1= cv2.imread('./Imagens/quadrados.png')
cv2.imshow('Imagem i1',I1)
print(I1.dtype)

I2 = np.float32(I1/255)
cv2.imshow('Imagem i2',I2)

I3=np.uint8(I2*255)
print(I3.dtype)
cv2.imshow('Imagem i3',I3)


cv2.waitKey(0)