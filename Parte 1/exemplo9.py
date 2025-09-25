import cv2
import numpy as np 
from matplotlib import pyplot as plt

I_bgr = cv2.imread('../Imagens/flowers4.png')
cv2.imshow('Imagem BGR',I_bgr)
cv2.waitKey(0)

B = I_bgr[:,:,0]  #canal azul
G = I_bgr[:,:,1]  #canal verde  
R = I_bgr[:,:,2]  #canal vermelho

I_cinza1 = np.uint8((1/3)*B + (1/3)*G + (1/3)*R) #conversao para cinza usando a media dos tres canais

cv2.imshow('Imagem Cinza1',I_cinza1)
cv2.waitKey(0)

I_cinza2= np.uint8(0.1140*B + 0.5870*G + 0.2989*R) #conversao para cinza usando a media dos tres canais

cv2.imshow('Imagem Cinza2',I_cinza2)
cv2.waitKey(0)

I_cinza3 = cv2.cvtColor(I_bgr, cv2.COLOR_BGR2GRAY) #conversao para cinza usando funcao do opencv
cv2.imshow('Imagem Cinza3',I_cinza3)
cv2.waitKey(0)
cv2.destroyAllWindows()  # Fecha todas as janelas ao final

# Alternativa: mostrar todas as imagens juntas usando matplotlib
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(I_bgr, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(I_cinza1, cmap='gray')
plt.title('Cinza1 (Média simples)')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(I_cinza2, cmap='gray')
plt.title('Cinza2 (Média ponderada)')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(I_cinza3, cmap='gray')
plt.title('Cinza3 (OpenCV)')
plt.axis('off')

plt.tight_layout()
plt.show()