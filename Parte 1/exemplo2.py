import cv2
import numpy as np
from matplotlib import pyplot as plt

#imagem 100 x 100

I = np.zeros((100,100),np.uint8)

R = 30
x0 = 50
y0=50

for theta in np.arange(0,360): #define theta aqui 
    xc = int(x0 + R * np.cos(np.deg2rad(theta)))
    yc = int(y0 + R * np.sin(np.deg2rad(theta)))
    I[yc,xc] = 255

plt.imshow(I, cmap='gray')
plt.show()
