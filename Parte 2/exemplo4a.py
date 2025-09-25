import cv2 

import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/monalisa2.png', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(I, cmap='gray')
plt.show()

#rotação
n_linhas,n_colunas = I.shape


cx = 0.2
cy = 0 


A=np.array([[1,cx,0],[cy,1,0]],np.float32)

n_linhas_final =int(n_linhas*(1+cy) )
n_colunas_final = int(n_colunas*(1+cx))

cv2.warpAffine(I,A,(n_colunas_final,n_linhas_final))

I2 = cv2.warpAffine(I,A,(n_colunas_final,n_linhas_final))
plt.figure()    
plt.imshow(I2, cmap='gray')
plt.show()