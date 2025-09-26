import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

# ===========================
# Parâmetros ajustáveis
# ===========================
VIDEO_PATH = 'sequencia1.mp4'
ref_bgr = (0, 255, 255)      # cor de referência (B, G, R) -> amarelo
tau = 150.0                  # limiar (distância euclidiana)
kernel = 3                   # tamanho do kernel (ímpar) para morfologia
min_pixels = 5               # mínimo de pixels brancos na coluna central
cooldown_frames = 8          # quadros de espera após contar um objeto

# ===========================
# Utilitários
# ===========================
def euclidean_distance_bgr(img_bgr, ref_bgr):
    B = img_bgr[:, :, 0].astype(np.float32)
    G = img_bgr[:, :, 1].astype(np.float32)
    R = img_bgr[:, :, 2].astype(np.float32)
    br, gr, rr = map(float, ref_bgr)
    D = np.sqrt((B - br) ** 2 + (G - gr) ** 2 + (R - rr) ** 2)
    return D

def binarize_by_threshold(D, tau):
    M = (D <= float(tau)).astype(np.uint8) * 255
    return M

def morph_cleanup(M, ksize=3):
    k = max(1, int(ksize))
    if k % 2 == 0:
        k += 1
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
    opened = cv2.morphologyEx(M, cv2.MORPH_OPEN, kernel, iterations=1)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=1)
    return closed

# ----------------------------------------------------------
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise SystemExit(f"Não foi possível abrir o vídeo: {VIDEO_PATH}")

n_linhas = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
n_colunas  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
if not fps or fps <= 0:
    fps = 30.0

# ----------------------------------------------------------
# Gera figura
fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3, adjustable='box', aspect=0.9)

fig_width = 20
fig_height = 6
fig.set_size_inches((fig_width/2.54, fig_height/2.54))
fig.tight_layout()

# ----------------------------------------------------------
ret = True

# Estado da contagem
count = 0
prev_present = False
cooldown = 0

# Estatística de tempo
t_sum = 0.0
n_timed = 0

# Loop principal
while ret:

    # lê frame do vídeo
    ret, I1 = cap.read()
    if not ret or I1 is None:
        break

    # ===== INÍCIO REGIÃO TEMPORIZADA =====
    tic = cv2.getTickCount()

    # Algoritmo de detecção de objetos
    # 1) Distância euclidiana para ref_bgr
    D = euclidean_distance_bgr(I1, ref_bgr)

    # 2) Binarização por tau
    I2 = binarize_by_threshold(D, tau)

    # 3) Limpeza morfológica
    I2 = morph_cleanup(I2, kernel)

    # 4) Coluna central + decisão de presença
    cx = n_colunas // 2
    col = I2[:, cx]
    white_count = int(np.count_nonzero(col == 255))
    present = (white_count >= min_pixels)

    # 5) Borda de subida + cooldown
    if present and (not prev_present) and cooldown == 0:
        count += 1
        cooldown = cooldown_frames
    prev_present = present
    if cooldown > 0:
        cooldown -= 1

    # ===== FIM REGIÃO TEMPORIZADA =====
    toc = cv2.getTickCount()
    t_proc = (toc - tic) / cv2.getTickFrequency()  # segundos
    t_sum += t_proc
    n_timed += 1

    # --- Atualiza plots ---
    ax1.clear()
    ax1.imshow(cv2.cvtColor(I1, cv2.COLOR_BGR2RGB))
    ax1.set_title(f"Frame original\nCount: {count}")

    ax2.clear()
    ax2.imshow(I2, cmap='gray', vmin=0, vmax=255)
    ax2.plot([n_colunas/2, n_colunas/2], [0, n_linhas-1], ':')
    ax2.set_title("Máscara binária + coluna central")

    # Coluna central 1D (opcional)
    ax3.clear()
    ax3.plot(np.arange(0, col.size), col)
    ax3.set_ylim([0, 260])
    ax3.set_xlim([0, col.size])
    ax3.set_title('Coluna central da\n imagem binária')

    # HUD de tempo
    t_ms = t_proc * 1000.0
    t_avg_ms = (t_sum / max(1, n_timed)) * 1000.0
    realtime_ok = t_proc <= (1.0 / fps)
    fig.suptitle(f"t_ms={t_ms:.2f} | t_avg={t_avg_ms:.2f} | 1/FPS={1000.0/fps:.2f} ms | REAL-TIME: {'OK' if realtime_ok else 'NO'}",
                 fontsize=10)

    plt.pause(0.001)

print('Processo finalizado!')
if n_timed > 0:
    t_avg_ms = (t_sum / n_timed) * 1000.0
    print(f"[RESULT] Contagem final = {count}")
    print(f"[RESULT] t_medio = {t_avg_ms:.2f} ms  |  1/FPS = {1000.0/fps:.2f} ms  |  REAL-TIME: {'OK' if (t_sum/n_timed) <= (1.0/fps) else 'NO'}")

cv2.waitKey(0)
