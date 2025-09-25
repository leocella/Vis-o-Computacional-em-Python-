import cv2
import numpy as np
from matplotlib import pyplot as plt 

M = 200
N = 400
I=np.zeros((M,N),dtype=np.uint8)


I [50:150, 20:380] = 255


for x in np.arange(20,380):
    for y in np.arange(50,150):
        I[y,x]=255 # valor referente a branco em imagens de 8 bits

#aprensentar a imagem   

#cv2.imshow("Imagem Binária",I)
#cv2.waitKey(0) # espera até que uma tecla seja pressionada

plt.figure()
plt.imshow(I, cmap='gray')
plt.title("Imagem Binária")
plt.axis("off")
plt.show()