import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1 y 1.1
ruta = "./img/" 
imagenes = [cv2.imread(os.path.join(ruta, f"{i}.jpg"), cv2.IMREAD_GRAYSCALE) for i in range(1, 17)]
imagenes = [img for img in imagenes if img is not None]
promedio = np.mean(imagenes, axis=0).astype(np.uint8)
cv2.imshow("Imagen Promedio", promedio)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1.2
ruido = cv2.absdiff(imagenes[0], promedio)
cv2.imshow("Imagen Ruido", ruido)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1.3
media_ruido = np.mean(ruido)
std_ruido = np.std(ruido)
print("Media del ruido:", media_ruido)
print("Desviación estándar del ruido:", std_ruido)

# 2
img_moon = cv2.imread("./img/tiff/imagen.tiff", cv2.IMREAD_GRAYSCALE)
print("Tamaño de la imagen:", img_moon.shape)

# 2.1
size = 21  
sigma = 5  

# Crear coordenadas (i,j = 1..21)
i = np.arange(1, size+1)
j = np.arange(1, size+1)
x, y = np.meshgrid(i, j)

# Fórmula Gaussiana con centro en (11,11)
gaussian_mask = (1/(2*np.pi*sigma**2)) * np.exp(-((x-11)**2 + (y-11)**2)/(2*sigma**2))
gaussian_mask /= np.sum(gaussian_mask)

# Configurar la figura y el gráfico 3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, gaussian_mask, cmap='viridis')
ax.set_title("Máscara Gaussiana 21x21 (σ=5)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Amplitude')
plt.show()

# 2.2
p = cv2.imread("./img/tiff/imagen.tiff", cv2.IMREAD_GRAYSCALE)

# Aplicar convolución con la máscara gaussiana
pl = cv2.filter2D(p, -1, gaussian_mask)

# Mostrar imágenes
plt.subplot(1,2,1)
plt.imshow(p, cmap='gray')
plt.title("Imagen original (p)")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(pl, cmap='gray')
plt.title("Imagen suavizada (pl)")
plt.axis("off")
plt.show()

# 2.3
ph = cv2.subtract(p, pl)

plt.imshow(ph, cmap='gray')
plt.title("Componente de alta frecuencia (ph)")
plt.axis("off")
plt.show()

# 2.4
A = 1.5 
pb = cv2.addWeighted(p, 1.0, ph, A, 0)

plt.figure(figsize=(14, 6))

plt.subplot(1, 3, 1)
plt.imshow(p, cmap="gray")
plt.title("Imagen Original (p)")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(pl, cmap="gray")
plt.title("Imagen Suavizada (pl)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(pb, cmap="gray")
plt.title(f"High Boost (A={A}, σ={sigma})")
plt.axis("off")

plt.show()

cv2.imwrite("moon_suavizada.png", pl)
cv2.imwrite("moon_highboost.png", pb)