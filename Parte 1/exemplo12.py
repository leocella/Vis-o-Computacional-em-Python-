import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/tomato_124.jpg')

#segmentação baseada em cor

r_ref = 166
g_ref = 32
b_ref = 33

delta = 20 #tolerância

B = I[:,:,0]
G = I[:,:,1]
R = I[:,:,2]

Mb = (R>=(r_ref-delta)) & (R<=(r_ref+delta)) 
Mg = (G>=(g_ref-delta)) & (G<=(g_ref+delta))
Mr = (B>=(b_ref-delta)) & (B<=(b_ref+delta))

M = Mb & Mg & Mr

#apresenta resultados
n_linhas,n_colunas,n_camadas = I.shape
Ibin = np.zeros((n_linhas,n_colunas),dtype=np.uint8)

Ibin[M] = 255

# Criar subplot com 1 linha e 2 colunas
plt.figure(figsize=(12, 5))

# Primeira imagem (original)
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

# Segunda imagem (segmentação)
plt.subplot(1, 2, 2)
plt.imshow(Ibin, cmap='gray')
plt.title('Segmentação por Cor')
plt.axis('off')

plt.tight_layout()
plt.show()



