import cv2 

import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/monalisa2.png', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(I, cmap='gray')
plt.show()

#rotação

theta = 30 #graus
theta_rad = np.deg2rad(theta)
n_linhas,n_colunas = I.shape

# Calcula as novas dimensões necessárias para conter toda a imagem rotacionada
n_linhas_final = int(abs(n_linhas*np.cos(theta_rad)) + abs(n_colunas*np.sin(theta_rad)))
n_colunas_final = int(abs(n_linhas*np.sin(theta_rad)) + abs(n_colunas*np.cos(theta_rad)))

# Centro da imagem original
cx_orig = n_colunas / 2
cy_orig = n_linhas / 2

# Centro da imagem final
cx_final = n_colunas_final / 2
cy_final = n_linhas_final / 2

# Matriz de rotação em torno do centro da imagem original
cos_theta = np.cos(theta_rad)
sin_theta = np.sin(theta_rad)

# Translação para mover o centro da imagem rotacionada para o centro da nova imagem
dx = cx_final - (cx_orig * cos_theta - cy_orig * sin_theta)
dy = cy_final - (cx_orig * sin_theta + cy_orig * cos_theta)

A = np.array([[cos_theta, -sin_theta, dx],
              [sin_theta, cos_theta, dy]], np.float32)

I2 = cv2.warpAffine(I,A,(n_colunas_final,n_linhas_final))
plt.figure()    
plt.imshow(I2, cmap='gray')
plt.show()