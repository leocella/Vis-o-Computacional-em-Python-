# LAB 1 — Atividade 1 (Guia em .md)

**Tarefa:** Contar quantos objetos **amarelos** cruzam a **coluna central** do vídeo `sequencia1.mp4`.

## Pipeline
1. **Segmentação por cor (BGR)** via **distância euclidiana** para uma cor de referência `[br, gr, rr]` (amarelo).
2. **Binarização** por limiar `τ`: pixels próximos da cor viram `255`; demais `0` → imagem `I2`.
3. **Pós-processamento morfológico** (open/close) para tirar ruído/preencher falhas.
4. **Coluna central**: extrair a coluna `x = W//2` de `I2` e decidir se **há objeto** (`present`) contando pixels brancos.
5. **Contagem**: quando `present` passa de **False → True** (borda de subida) e `cooldown==0`, **incrementar `count`** e armar `cooldown`.
6. **Tempo por quadro**: medir entre o fim de `cap.read()` e o término da decisão (`present` + possível contagem).
7. **Tempo médio** vs `1/FPS` do arquivo → indicar **REAL‑TIME OK/NO**.

## Parâmetros (no topo do script)
- `ref_bgr = (0, 255, 255)`  *(amarelo, BGR)*
- `tau = 150.0`  *(limiar de distância)*
- `kernel = 3`  *(morfologia)*
- `min_pixels = 5`  *(mínimo de brancos na coluna)*
- `cooldown_frames = 8`

## Como rodar
```bash
pip install opencv-python numpy matplotlib
python lab1_atividade1_resolvido.py  # coloque sequencia1.mp4 na mesma pasta
```

## Critérios de checagem
- [ ] Leitura do vídeo e FPS obtido.
- [ ] Distância euclidiana BGR + limiar `τ` → `I2` binária.
- [ ] Limpeza morfológica (open/close).
- [ ] Extração da coluna central e decisão por `min_pixels`.
- [ ] Borda de subida + `cooldown` para não recontar.
- [ ] Tempo por quadro e tempo médio corretos.
- [ ] Comparação com `1/FPS` e indicação `REAL‑TIME OK/NO` no HUD/prints.