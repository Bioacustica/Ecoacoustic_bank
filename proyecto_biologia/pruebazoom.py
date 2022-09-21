import numpy as np
import imutils
import cv2

img1 = cv2.imread("C:\\Projects\\proyecto_biologia\\firma.jpg")
height, width = img1.shape[:2]
img = np.zeros((height, width, 3), np.uint8) 
img = img1.copy() 

drawing = False
mode = True
ix, iy = -1, -1
def draw(event, x, y, flags, param): # Se declara la funcion
    global ix, iy, drawing, mode, xf, yf  # Defino unas variables globales

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
        drawing = True  # En caso de ser verdado se asigna una variable boleana
        ix, iy = x, y  # Almacenamos la poscion incial en las variales

    elif event == cv2.EVENT_MOUSEMOVE:  # Cuando se mueva el moue
        if drawing == True:  # Si se verdadera la condicion de dibujo
            if mode == True: # Si se verdadera la condicion de modo
                img[0:height, 0:width] = (img1[0:height, 0:width])
                cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), thickness=2,) 

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False 
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness=2)
            xf=x
            yf=y
            
            if xf<ix and yf < iy:
               yf=iy
               xf=ix
               iy=y
               ix=x
            elif xf<ix:
                xf=ix
                ix=x
            elif yf < iy:
                yf=iy
                iy=y

img = np.zeros((height, width, 3), np.uint8) 
img[0:height, 0:width] = (img1[0:height, 0:width])
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(ix, iy)
        # Se esperan 30mins para el cierre de la ventana o hasta que el usuario precione la tecla q
        break

resultado = imutils.resize(img1, height=iy, width=ix)
cv2.imshow('resultado',resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()