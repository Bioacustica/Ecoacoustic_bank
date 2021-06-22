
import sys

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
#from matplotlib import cm


def cargar_audio(audio_seleccionado):
    '''
    Esta función permite cargar el audio seleccionado por la libreria de librosa

    :param audio_seleccionado: recibe la ruta donde se encuentra el audio a leer
    :type audio_seleccionado: str

    :return: audio no encontrado si la ruta no existe o el archivo de audio cargado 
    :rtype: un array numpy
    '''
    try:
        return librosa.load(audio_seleccionado, sr=48000)
    except FileNotFoundError:
        sys.exit('Audio no encontrado')


def mostrar_waveplot(y, sr):
    plt.figure(figsize=(14, 5))
    # plotting the sampled signal
    librosa.display.waveplot(y, sr=sr)
    plt.show()


def mostrar_espectograma(y, sr):
    '''
    Esta función permite cargar el audio seleccionado por la libreria de librosa

    :param y: una tupla de la conversion del audio a un array
    :type y: tuple

    :param fs: genera el valor de los Decibels relative to full scale
    :type fs: Int

    :return: no return, genera la gráfica espectograma 
    :rtype: grafico
    '''
    tam_ven = 1024
    hop = int(np.round(tam_ven/4))
    nfft = int(np.round(2*tam_ven))
    ventana = signal.windows.blackman(tam_ven, sym=False)
    numpy_arr = librosa.stft(y, hop_length=hop, n_fft=nfft,
                             window=ventana,
                             win_length=tam_ven)
    #x_db = 10 * np.log10(numpy_arr)
    x_db = librosa.amplitude_to_db(np.abs(numpy_arr))
    plt.figure(figsize=(10, 5))
    librosa.display.specshow(
        x_db, sr=sr, y_axis='linear', x_axis='s', hop_length=hop,
        cmap='rainbow')  # cmap = cm.jet
    plt.colorbar()
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")
    plt.show()
    print(x_db)


def mostrar_grafico(grafico_seleccionado, y, sr):
    if grafico_seleccionado and (
            grafico_seleccionado.lower() == 'w'
            or grafico_seleccionado.lower() == 'waveplot'):
        mostrar_waveplot(y, sr)
    if grafico_seleccionado and (
            grafico_seleccionado.lower() == 'e'
            or grafico_seleccionado.lower() == 'espectograma'):
        mostrar_espectograma(y, sr)
    else:
        print('no puedo mostrar grafico')


def mostrar_grafico_ui(audio_seleccionado, grafico_seleccionado):
    y, sr = cargar_audio(audio_seleccionado)
    mostrar_grafico(grafico_seleccionado, y, sr)


if __name__ == '__main__':
    audio_entrada = input("Elije la ruta del audio:")
    y, sr = cargar_audio(audio_entrada)
    grafico_entrada = input(
        "Elije la salida (w = waveplot / e = espectograma):")
    mostrar_grafico(grafico_entrada, y, sr)
