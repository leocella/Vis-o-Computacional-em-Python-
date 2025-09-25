import cv2 
import numpy as np
from matplotlib import pyplot as plt
import visaoComputacional as visco

cap = cv2.VideoCapture('Imagens/camera_vigilancia.avi')
n_linhas = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
n_colunas = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


#criar buffer para armazenar os frames

tamanho_buffer = 24
buffer = visco.videoBuffer((n_linhas, n_colunas), tamanho_buffer)


while cap.isOpened():
    ret, I1 = cap.read() # retorna ret e frame (I1)
    if not ret:
        print("Não foi possível capturar o vídeo")
        break

    I2 = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)

    # inserir frame no buffer
    buffer.insereFrame(I2.copy())

    #detectação de movimento 

    I3 = np.uint8(np.abs(np.float32(buffer.primeiroFrame()) -\
                     np.float32(buffer.ultimoFrame())))

    #binarização da imagem
    limiar = 100
    I4 = cv2.threshold(I3, limiar, 255, None, cv2.THRESH_BINARY)     
    cv2.imshow('Video', I3)
        
        
        
    if cv2.waitKey(1)  == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()