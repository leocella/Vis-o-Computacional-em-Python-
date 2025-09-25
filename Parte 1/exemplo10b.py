import cv2
import numpy as np 
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/castle.jpg', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(I,cmap = 'gray')


### Histograma ###
hist = cv2.calcHist([I], [0], None, [256], [0, 256])  # Usando função do OpenCV

n_linhas,n_colunas = I.shape

for x in np.arange(0,n_colunas):
    for y in np.arange(0,n_linhas):
        c = I[y,x]
        hist[c] = hist[c] + 1

plt.figure()
plt.bar(np.arange(0,256), hist[:,0])  # Ajuste para exibir corretamente o histograma    
plt.xlim([0, 256])
plt.title('Histograma')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.show()