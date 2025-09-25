import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Leer imagen RGB y mostrar canales 
img = cv2.imread("./img/image.png")  
b, g, r = cv2.split(img)

cv2.imshow("Original", img)
cv2.imshow("Canal Rojo", r)
cv2.imshow("Canal Verde", g)
cv2.imshow("Canal Azul", b)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2. Conversión de espacio de color 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
yuv  = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("Grises", gray)
cv2.imshow("YUV", yuv)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Recorte de imagen.bmp
# imagen recortada hacia la esquina inferior derecha
bmp = cv2.imread("./img/image.bmp")
alto, ancho = bmp.shape[:2]
crop = bmp[alto//3:, ancho//3:]  
cv2.imshow("Recorte", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Leer imagen .pcx 
'''¿
cv2.VideoCapture resultó más compatible que cv2.imread para .pcx. Esto demuestra que, aunque OpenCV está optimizado para formatos modernos, en ocasiones es necesario probar distintos métodos o usar librerías complementarias (como Pillow) para trabajar con formatos antiguos.
'''
# Método 1
pcx = cv2.imread("./img/image.pcx")          
# Método 2
cap = cv2.VideoCapture("./img/image.pcx")   
ret, pcx2 = cap.read()
if ret:
    cv2.imshow("PCX cap", pcx2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print("PCX:", pcx)

# 5. Imagen .png y mostrar canales
png = cv2.imread("./img/image.png")
b, g, r = cv2.split(png)
cv2.imshow("Canal Rojo PNG", r)
cv2.imshow("Canal Verde PNG", g)
cv2.imshow("Canal Azul PNG", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Imagen .jpg con paletas predefinidas 
img = cv2.imread("./img/image.jpg")  
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for cmap in [cv2.COLORMAP_JET, cv2.COLORMAP_HOT, cv2.COLORMAP_OCEAN]:
    colored = cv2.applyColorMap(img_gray, cmap)
    cv2.imshow(f"Mapa {cmap}", colored)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Rotaciones 
rot90  = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rot180 = cv2.rotate(img, cv2.ROTATE_180)

(h, w) = img.shape[:2]
centro = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(centro, 45, 1.0)  
rot45 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Original", img)
cv2.imshow("Rotada 45", rot45)
cv2.imshow("Rotada 90", rot90)
cv2.imshow("Rotada 180", rot180)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Guardar en TIFF 
img = cv2.imread("./img/image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("imagen.tiff", gray) 