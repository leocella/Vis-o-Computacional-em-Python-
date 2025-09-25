import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('./Imagens/tomato_124.jpg')

plt.figure()
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.show()

#segmentação baseada em cor

cor_ref = np.array([32, 32, 166])  # RGB

delta = 20 #tolerância

limiar_superior = cor_ref + delta
limiar_inferior = cor_ref - delta

cv2.inRange(I, limiar_inferior, limiar_superior)

Ibin = cv2.inRange(I, limiar_inferior, limiar_superior)

plt.figure()
plt.imshow(Ibin,cmap='gray')
plt.show()