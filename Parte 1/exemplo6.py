import cv2
import numpy as np # renomeando numpy para np para facilitar na hora de chamar as funcoes
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/quadrados.png')


print(I.shape)
print(I.dtype)
print(I)

cv2.imshow('Imagem BGR',I)
cv2.waitKey(0)

plt.figure()
plt.imshow(cv2.cvtColor(I,cv2.COLOR_BGR2RGB))
plt.show()