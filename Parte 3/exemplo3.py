import cv2
import numpy as np
from matplotlib import pyplot as plt

I_1  = cv2.imread('Imagens/castle.jpg', cv2.IMREAD_GRAYSCALE)

# Apresenta imagem original I_1
plt.figure()
plt.imshow(I_1, cmap='gray')
plt.title('Imagem original I_1')

# Histograma da imagem original I_1
hist_I1 = cv2.calcHist([I_1], [0], None, [256], [0,256])


# ALTERAÇÃO DO BRILHO

I_2 = 255 - I_1


hist_I2 = cv2.calcHist([I_2], [0], None, [256], [0,256])


# Apresenta I_2
plt.figure()
plt.imshow(I_2, cmap='gray')
plt.title('Imagem I_2 (com aumento de brilho)')

# Calcula histograma do I_2


# Apresenta histograma da imagem original I_1
plt.figure()
plt.bar(np.arange(0,256), hist_I1[:,0])
plt.xlim([0,256])
plt.title('Histograma da Imagem Original I_1')
plt.xlabel('Valores dos pixels')
plt.ylabel('Número de pixels')

# Apresenta histograma da imagem I_2
plt.figure()
plt.bar(np.arange(0,256), hist_I2[:,0])
plt.xlim([0,256])
plt.title('Histograma da Imagem I_2 (com aumento de brilho)')
plt.xlabel('Valores dos pixels')
plt.ylabel('Número de pixels')


plt.show()


hist_I2=cv2.calcHist([I_2], [0], None, [256], [0,256])

fig,axs = plt.subplots(2,2,figsize=(8,8))
axs[0,0].imshow(I_1, cmap='gray')
axs[0,1].bar(np.arange(0,256), hist_I1[:,0])
axs[1,0].imshow(I_2, cmap='gray')
axs[1,1].bar(np.arange(0,256), hist_I2[:,0])
plt.show()
