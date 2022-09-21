import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from matplotlib.mlab import specgram
#from recorte import draw


def cargar_audio(audio_seleccionado):
    muestra, senial = wavfile.read(audio_seleccionado)
    return muestra, senial

def mostrar_espectograma(audio_seleccionado):
    color = 'inferno' #@param ["magma", "inferno", "rainbow"]
    muestra, senial = cargar_audio(audio_seleccionado)
    plt.rcParams['axes.grid'] = False
    plt.specgram(senial, Fs=muestra, cmap=color)
    plt.show()

def mostrar_grafico(audio_seleccionado):
    mostrar_espectograma(audio_seleccionado)


    
if __name__ == '__main__':
    audio_entrada = input("Elije la ruta del audio:")
    mostrar_grafico(audio_entrada)
    audio_entrada.draw() 