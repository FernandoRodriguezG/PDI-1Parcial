import cv2
import numpy as np

def filtroSobel(img):
    sobelX = cv2.Sobel(img,cv2.CV_16S,1,0)
    sobelY = cv2.Sobel(img,cv2.CV_16S,0,1)
    absX = cv2.convertScaleAbs(sobelX)
    absY = cv2.convertScaleAbs(sobelY)
    return cv2.addWeighted(absX,0.8,absY,0.8,0)
    
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

def filtroBilateral(img):
    b = cv2.bilateralFilter(img,15,5,5)
    return b

def filtroBlur(img):
    ksize = (3,3)
    return cv2.blur(img,ksize)

def gauBlur(img):
    return cv2.GaussianBlur(img, (3,3),0) 

def filtroMedian(img):
    return cv2.medianBlur(img,3)

#Ejecucion principal del programa
img = cv2.imread(r"examen_b.tif") #Abrimos imagen
d = dilatacion(img,1)
s = filtroSobel(d)
b = gauBlur(s)
final = cortar(rotar(b))
cv2.imshow('P1_Fernando_Rodriguez',final) #Muestra imagen
cv2.waitKey(0)
cv2.destroyAllWindows()