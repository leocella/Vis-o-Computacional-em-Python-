import cv2
import numpy as np # renomeando numpy para np para facilitar na hora de chamar as funcoes
from matplotlib import pyplot as plt

M = 200
N = 400

I = np.zeros((M,N), dtype=np.uint8) #criando uma imagem de 200 x 400 pixels, com todos os valores iguais a zero (preto)

for x in np.arange(0,N): #percorrendo todas as colunas
   c = np.uint8(x*255/(N-1)) ## coloca no tipo de dado uint8
   I [:,x] = c # atribuindo o valor c a todas as linhas da coluna x

#apresentar imagem
plt.figure()
plt.imshow(I, cmap='gray')
plt.show()

