import cv2
import numpy as np
from matplotlib import pyplot as plt

I_1  = cv2.imread('Imagens/castle.jpg', cv2.IMREAD_GRAYSCALE)



# Histograma da imagem original I_1
hist_I1 = cv2.calcHist([I_1], [0], None, [256], [0,256])
hist_I1 = hist_I1[:,0]


#PDF ( função densidade de probabilidade)
pdf = hist_I1/(I_1.size)

#funcao de distribuição acumulada

cdf = np.cumsum(pdf)
print(cdf)


#função de mapeamento

f = 255*cdf

#equalização

n_linhas, n_colunas = I_1.shape
I_2 = np.zeros((n_linhas, n_colunas), dtype=np.uint8)

for x in np.arange(0,n_colunas):
    for y in np.arange(0,n_linhas):
        I_2[y,x] = f[I_1[y,x]]


hist_I2=cv2.calcHist([I_2], [0], None, [256], [0,256])
hist_I2=hist_I2[:,0]

fig,axs = plt.subplots(2,2,figsize=(8,8))
axs[0,0].imshow(I_1, cmap='gray')
axs[0,1].bar(np.arange(0,256), hist_I1)
axs[1,0].imshow(I_2, cmap='gray')
axs[1,1].bar(np.arange(0,256), hist_I2)
plt.show()
