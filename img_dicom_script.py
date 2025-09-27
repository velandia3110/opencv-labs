import pydicom
import os
import cv2

# Ruta a la carpeta DICOM
folder = "./img/dicom/"

# Listar archivos DICOM
dicom_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".dcm")]

# Ordenar por nombre
dicom_files.sort()

# Leer imágenes
images = [pydicom.dcmread(f).pixel_array for f in dicom_files]

# Mostrar todas las imágenes 
for i, img in enumerate(images):
    cv2.imshow("Simulacion DICOM", img)
    print(f"Mostrando imagen {i+1}/{len(images)}")
    cv2.waitKey(500)  

cv2.destroyAllWindows()
