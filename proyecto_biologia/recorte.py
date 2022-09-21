import cv2
import os
import numpy as np


xi, yi = 0, 0
xf, yf = 0, 0
drawing = False


def draw(event, x, y, flags, param): 
    # Se declara la funcion globales
    global xi, yi, drawing, xf, yf, img, img2

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
         # En caso de ser verdado se asigna una variable boleana
        xi, yi = x, y 
        drawing = False
   
 #Se confirma cuando se suelte el evento clic,
    elif event == cv2.EVENT_LBUTTONUP:
        xf, yf = x, y
        drawing = True 
        #se toman los valores trazados y se recorta el tramo de la imagen seleccionada
        imgPart = img[yi:yf, xi:xf,:]
        cv2.imwrite("recorte.png",imgPart)
        img2 = cv2.imread("recorte.png")#Se guarda el recorte realizado
        cv2.namedWindow(winname="zoom")
        img2 = cv2.resize(img2, None, fx=3,fy=3)   #se le aplica zoom al recorte seleccionado
        cv2.imshow("zoom",img2)
   
 #Se lee el espectrograma          
img = cv2.imread("C:\\Projects\\proyecto_biologia\\Figure_1.png")            
cv2.namedWindow(winname="imagen") #se genera ventana para mostrar la imagen resultante
cv2.setMouseCallback("imagen",draw) # se hace el llamado para mostrar espectrograma
'''
#Crear carpeta para guardar las imagenes que se les aplica el zoom
output_images = "C:\\Projects\\proyecto_biologia\\recortes" #ruta de creación
if not os.path.exists(output_images):
        os.makedirs(output_images)
        print("Directorio creado", output_images)'''
while True:
    if drawing==True: #Se toman los valores del rectangulo trazado en el evento mouse.
        cv2.rectangle(img, (xi,yi), (xf,yf), (0, 0, 255), thickness=2) #se pinta el recuadro trazado
        

    cv2.imshow("imagen",img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        print(xi, yi)
        break
cv2.destroyAllWindows()