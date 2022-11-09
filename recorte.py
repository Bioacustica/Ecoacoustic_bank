from turtle import position
import cv2
import os
import numpy as np
from csv import writer
from tkinter import * 


xi, yi = 0, 0
xf, yf = 0, 0
drawing = False

def draw(event, x, y, flags, param): 
    # Se declara la funcion globales
    global xi, yi, drawing, xf, yf, img, img2, count

    if event == cv2.EVENT_LBUTTONDOWN:  # Se pregunta si se ha presionado el mouse
         # En caso de ser verdado se asigna una variable boleana
        xi, yi = x, y 
        drawing = False
        count += 1   #Contador para el indice del zoom
        #save_coordinates('CSV_file.csv',x,y)
    #Se confirma cuando se suelte el evento clic,
    elif event == cv2.EVENT_LBUTTONUP:
        #Se toman los valores de x, y para que se puedan interpretar como posición final y se cambia la variable drawing a verdadero
        xf, yf = x, y
        drawing = True 
        save_coordinates('CSV_fileZoom.csv',x,y)
        #Se toman los valores trazados y se recorta el tramo de la imagen seleccionada
        imgPart = img[yi:yf, xi:xf,:]
        #Se aplica el zoom al recorte anterior
        imgPart = cv2.resize(imgPart, None, fx=3,fy=3)  
        #Se guarda el zoom realizado en la carpeta creada con su formato y numeración
        cv2.imwrite(output_images + "/zoom_" + str(count) + ".png", imgPart)
        #Se carga el zoom y muestra en una nueva ventana 
        img2 = cv2.imread(output_images + "/zoom_" + str(count) + ".png")
        cv2.namedWindow(winname="zoom")
        cv2.imshow("zoom",img2)
        
###### EN PRUEBA #########
    if event == cv2.EVENT_RBUTTONDOWN:
        text = input("Nombre etiqueta: ")
        cv2.putText(img,text,(x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)        
        cv2.imshow("imagen", img)
        

'''
        font = cv2.FONT_HERSHEY_SIMPLEX
        position = (x,y)
        fontScale = 2
        fontColor = (255,255,255)

        cv2.putText(img,"Hola!",
            font,
            position,
            fontScale,
            fontColor)
        cv2.imshow("imagen", img)
'''


def save_coordinates(filename,x,y):

    # The data assigned to the list
    data = [x,y]
    with open(filename, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data)
        f_object.close()
    if not os.path.exists('CSV_fileZoom.csv'):
            os.makedirs('CSV_fileZoom.csv')
 
   
 #Se lee el espectrograma          
img = cv2.imread("C:\\Projects\\SpectrogramUtilities\\Spectrogram.png")            
cv2.namedWindow(winname="imagen") #se genera ventana para mostrar la imagen resultante
cv2.setMouseCallback("imagen",draw) # se hace el llamado para mostrar espectrograma

#Crear carpeta para guardar las imagenes que se les aplica el zoom
output_images = "C:/Projects/SpectrogramUtilities/image_zoom" #ruta de creación
if not os.path.exists(output_images):
        os.makedirs(output_images)
        print("Directorio creado", output_images)
count = 0        

while True:
    if drawing==True: #Se toman los valores del rectangulo trazado en el evento mouse.
        cv2.rectangle(img, (xi,yi), (xf,yf), (0, 0, 255), thickness=2) #se pinta el recuadro trazado
        #count += 1 #contador para darle su respectiva numeración al recorte seleccionado.
    

    cv2.imshow("imagen",img)
   #cerramos el programa presionando la tecla Esc 
    if cv2.waitKey(1) & 0xFF == 27:
        print(xi, yi)
        
        break
cv2.destroyAllWindows()

  
