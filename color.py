
import cv2
import numpy as np
  

captura = cv2.VideoCapture(0) #habilitaamos la camrara
  
while(1):  
      
    #Capturamos una imagen y la convertimos de RGB -> HSV
    ret, imagen = captura.read()
    if(ret):
            hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
  
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro
            verde_bajos = np.array([49,50,50], dtype=np.uint8)
            verde_altos = np.array([80, 255, 255], dtype=np.uint8)
  
    #Crear una mascara con solo los pixeles dentro del rango de verdes
            mask = cv2.inRange(hsv, verde_bajos, verde_altos)
  
    #Encontrar el area de los objetos que detecta la camara
            momento = cv2.moments(mask)
            area = momento['m00']
  
    #Descomentar para ver el area por pantalla
    #print area
            if(area > 6000):
          
        #Buscamos el centro x, y del objeto
                x = int(momento['m10']/momento['m00'])
                y = int(momento['m01']/momento['m00'])
          
        #Mostramos sus coordenadas por pantalla
                print "x = ", x
                print "y = ", y
  
        #Dibujamos una marca en el centro del objeto
                cv2.rectangle(imagen, (x, y), (x+20, y+20),(0,0,255), 2)
      
      
    #Mostramos la imagen original con la marca del centro y
    #la mascara
            cv2.imshow('mask', mask)
            cv2.imshow('Camara', imagen)
            tecla = cv2.waitKey(5) & 0xFF
            if tecla == 27:
                break
  
cv2.destroyAllWindows()
