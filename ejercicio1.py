import cv2
import numpy as np

#cargamos imagen
image = cv2.imread('static/bainia.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#obtener dimensiones de la imagen
hight, width = image.shape[:2]
center = (width/2, hight/2)

#rotar la imagen
angulo = 45
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, hight))
cv2.imshow('Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

#definir la matriz de traslacion
tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

#aplicar la matriz de traslacion a la imagen
translated = cv2.warpAffine(image, M, (width, hight))
cv2.imshow('Image', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Deifnir la nueva altura y ancho de la imagen
new_width = 200
new_height = 300

#redimensionar la imagen
scaled = cv2.resize(image, (new_width, new_height))
cv2.imshow('Image', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

#recortar la imagen
x, y, w, h = 100, 100, 200, 150

#recortar region de interes ROI
cropped = image[y:y+h, x:x+w]

#Mostrar la imagen recortada
cv2.imshow('Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

#suavizado
smoothed = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Image', smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()

#realce
#definir el kernel para el filtro de afilado
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

#aplicar el filtro de afilado
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Deteccion de bordes
#cargar la imagen en escala de grises
image = cv2.imread('static/bainia.jpg', cv2.IMREAD_GRAYSCALE)

#aplicar el operador sobel para detectar los bordes
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

#combinar la respuesta de magnitud
edges = cv2.magnitude(sobelx, sobely)

#Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

#Mostrar la imagen con los bordes detectados
cv2.imshow('Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Imagen 1 = Goku
#Imagen 2 = Naruto
#Imagen 3 = Harry Potter
#Imagen 4 = Soilor Moon
#Imagen 5 = Ranma 1/2
#Imagen 6 = Pokemon
#Imagen 7 = Supercampenones