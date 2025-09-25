import cv2
import numpy as np # renomeando numpy para np para facilitar na hora de chamar as funcoes
from matplotlib import pyplot as plt

#BGR formato padrao de leitura de imagens


M=200
N=400

I=np.zeros((M,N,3),dtype=np.uint8)
#Camada verde
I[50:150,20:380,1]=255

#camada vermelha

I[50:150,20:380,2]=255

cv2.imshow('Imagem Colorida',I)
cv2.waitKey(0)

plt.figure()
plt.imshow(cv2.cvtColor(I,cv2.COLOR_BGR2RGB))
plt.title('Imagem Colorida I')
plt.show()
