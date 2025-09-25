import cv2 
import numpy as np
from matplotlib import pyplot as plt


Ifundo = cv2.imread('Imagens/agua2.png', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(Ifundo, cmap='gray')

Ipeixes = cv2.imread('Imagens/peixes2.png',cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(Ipeixes, cmap='gray')
plt.show()

#fusão das imagens

alfa = 0.3
I3 = Ifundo * alfa + Ipeixes * (1 - alfa)
I3 = np.uint8(I3)
plt.figure()
plt.imshow(I3, cmap='gray')
plt.show()
