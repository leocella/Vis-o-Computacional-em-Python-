import cv2
import numpy as np
from matplotlib import pyplot as plt

I1 = cv2.imread('Imagens/greenscreen.jpg')

#segmentaçao baseada em cor/geração da máscara
cor_ref = np.array([99,212,168])
delta = 40
M1 = cv2.inRange(I1, cor_ref - delta, cor_ref + delta)

#Obtenção do negativo da máscara
M2 = 255 - M1

# Exibir todas as imagens em subplots
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(I1, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(M1, cmap='gray')
plt.title('Máscara M1')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(M2, cmap='gray')
plt.title('Máscara M2 (Negativo)')
plt.axis('off')

plt.tight_layout()


#operação lógica AND e a mascara M2

I2=cv2.bitwise_and(I1, I1, mask=M2)
plt.subplot(1, 4, 4)
plt.imshow(cv2.cvtColor(I2, cv2.COLOR_BGR2RGB))
plt.title('Imagem I2')
plt.axis('off')


plt.show()