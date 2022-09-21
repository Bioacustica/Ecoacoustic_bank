import numpy as np
import cv2

img = cv2.imread("C:\\Projects\\proyecto_biologia\\pokemon.png")

height, width = img.shape[:2]
img[0:height, 0:width] = (img[0:height, 0:width])

drawing = False
valx = 0
valy = 0
mode = True

#función dibujar

def draw(event, x, y, flags, param): # Se declara la funcion
    global valx, valy, drawing, xf, yf  # Se definen vables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        valx, valy = x, y  # Almacenamos la poscion incial en las variales

    elif event == cv2.EVENT_MOUSEMOVE:  # Cuando se mueva el moue
        if drawing:
            cv2.rectangle(img, (valx,valy), (x,y), (0, 0, 255), thickness=2)
            img[0:height, 0:width] = (img[0:height, 0:width])
                #cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), thickness=2,) 
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False 
        cv2.rectangle(img, (valx,valy), (x,y), (0, 255, 0), thickness=2)
        xf=x
        yf=y
            
        if xf<valx and yf < valy:
            yf,xf=valy,valx
            valx,valy=x,y
        elif xf<valx:
            xf=valx
            valx=x
        elif yf < valy:
            yf=valy
            valy=y
#Conectar función draw con la imagen.

cv2.namedWindow(winname="imagen")
cv2.setMouseCallback("imagen",draw)



while True:
    cv2.imshow("imagen",img)
    if cv2.waitKey(10) & 0xFF == 27:
        print(valx, valy)
        break
cv2.destroyAllWindows()

'''
img = cv2.resize(img, None, fx=5, fy=4)


cv2.imshow("Imagen", img)
cv2.waitKey()'''








    
