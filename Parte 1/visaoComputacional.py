import cv2
import numpy as np 
from matplotlib import pyplot as plt


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