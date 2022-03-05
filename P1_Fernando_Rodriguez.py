import cv2
import numpy as np

def filtroSobel(img):
    sobelX = cv2.Sobel(img,cv2.CV_16S,1,0)
    sobelY = cv2.Sobel(img,cv2.CV_16S,0,1)
    absX = cv2.convertScaleAbs(sobelX)
    absY = cv2.convertScaleAbs(sobelY)
    return cv2.addWeighted(absX,0.5,absY,0.5,0)
    
def dilatacion(img,it):
    k = np.ones((3,3),np.uint8)
    return cv2.dilate(img,k,iterations=it)
    
def rotar(img):
    ancho = img.shape[1] #Se obtiene el numero de columnas
    alto = img.shape[0] #Se obtiene el numero de filas
    matrizRotacion = cv2.getRotationMatrix2D((ancho/2,alto/2),-15,1) #Se rota imagen, parametros: centro de rotacion, angulo y escala
    return cv2.warpAffine(img,matrizRotacion,(ancho,alto)) #Parametros: entrada, la matriz de rotacion, ancho y alto de la imagen

def cortar(img):
    return img[80:420,240:595] #Se recorta la imagen -> filaInicial:filaFinal,ColInicial:colFinal

def perfilado(img):
    gb = cv2.GaussianBlur(img,(9,9),5)
    return cv2.addWeighted(img,13.5,gb,-12.5,0)

#Ejecucion principal del programa
img = cv2.imread(r"examen_b.tif")
img_dilatacion = dilatacion(img,2)
img_sobel = filtroSobel(img_dilatacion)
img_perfilado = perfilado(img_sobel)
img_rotada = rotar(img_perfilado)
img_cortada = cortar(img_rotada)
cv2.imshow('P1_Fernando_Rodriguez',img_cortada) 
cv2.waitKey(0)
cv2.destroyAllWindows()