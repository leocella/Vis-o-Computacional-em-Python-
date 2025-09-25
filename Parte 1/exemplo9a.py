import cv2
import numpy as np 
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/castle.jpg',cv2.IMREAD_GRAYSCALE) #lendo a imagem em tons de cinza
plt.figure()
plt.imshow(I, cmap='gray')
plt.show()


L = 170
ret, O = cv2.threshold(I,L,255,None,cv2.THRESH_BINARY)



#linearizaçao global
def limiarizacao_global1(I,L):

    nlihas, n_colunas = I.shape
    O = np.zeros((nlihas,n_colunas), dtype=np.uint8)

    for x in np.arange(0,n_colunas): #percorrendo todas as colunas
        for y in np.arange(0,nlihas): #percorrendo todas as linhas
            if I[y,x] >= L:
                O[y,x] = 255
    return O




def limiarizacao_global2(I,L):

    nlinhas, n_colunas = I.shape
    O = np.zeros((nlinhas,n_colunas), dtype=np.uint8)

    for x in np.arange(0,n_colunas): #percorrendo todas as colunas
        for y in np.arange(0,nlinhas): #percorrendo todas as linhas
            if I[y,x] >= L:
                O[y,x] = 255
    return O
#---------------------#

I = cv2.imread('./Imagens/castle.jpg',cv2.IMREAD_GRAYSCALE) #lendo a imagem em tons de cinza
plt.figure()
plt.imshow(I, cmap='gray')

#linearizacao
L= 128
O=limiarizacao_global2(I,L)

plt.figure()
plt.imshow(O, cmap='gray')
plt.show()


          