# Abrir un archivo de audio .wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# INGRESO 
# archivo = input('archivo de sonido:' )
archivo = 'muestra_Ambiente.wav'
muestreo, sonido = waves.read(archivo)

# PROCEDIMIENTO
tamano=np.shape(sonido)
canales=len(tamano)
tipo = 'estéreo'
if (canales<2):
    tipo = 'monofónico'
duracion = len(sonido) /muestreo

# SALIDA
print('muestreo (Hz) : ',muestreo)
print('canales: ' + str(canales) + ' tipo ' + tipo )
print('duración (s): ',duracion)
print('tamaño de matriz: ', tamano)
print(sonido)
plt.plot(sonido)
plt.show()