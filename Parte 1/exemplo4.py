import cv2
import numpy as np # renomeando numpy para np para facilitar na hora de chamar as funcoes
from matplotlib import pyplot as plt


I = cv2.imread('./Imagens/quadrados_cinzas.png',cv2.IMREAD_GRAYSCALE)

print(I.shape)
print(I)

print(I[100,100])
print(I[100,300])
print(I[300,100])
print(I[300,300])



plt.imshow(I, cmap='gray')
plt.show()
