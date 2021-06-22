
import sys

import matplotlib.pyplot as plt
import numpy as np
import parselmouth
import seaborn as sns

sns.set()
plt.rcParams['figure.dpi'] = 100


def cargar_audio(audio_seleccionado):
    try:
        return parselmouth.Sound(audio_seleccionado)
    except parselmouth.PraatError:
        sys.exit('Audio no encontrado')


def mostrar_waveplot(snd):
    plt.figure()
    plt.plot(snd.xs(), snd.values.T)
    plt.xlim([snd.xmin, snd.xmax])
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.show()


def generar_espectograma(espectrograma, rango_dinamico=70):
    X, Y = espectrograma.x_grid(), espectrograma.y_grid()
    sg_db = 10 * np.log10(espectrograma.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() -
                   rango_dinamico, cmap='rainbow')
    plt.ylim([espectrograma.ymin, espectrograma.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")


def dibujar_intensidad(intensidad):
    plt.plot(intensidad.xs(), intensidad.values.T, linewidth=3, color='w')
    plt.plot(intensidad.xs(), intensidad.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")


def mostrar_espectograma(snd):
    intensity = snd.to_intensity()
    spectrogram = snd.to_spectrogram()
    plt.figure()
    generar_espectograma(spectrogram)
    plt.twinx()
    dibujar_intensidad(intensity)
    plt.xlim([snd.xmin, snd.xmax])
    plt.show()


def mostrar_grafico(grafico_seleccionado, snd):
    if grafico_seleccionado and (
            grafico_seleccionado.lower() == 'w'
            or grafico_seleccionado.lower() == 'waveplot'):
        mostrar_waveplot(snd)
    if grafico_seleccionado and (
            grafico_seleccionado.lower() == 'e'
            or grafico_seleccionado.lower() == 'espectograma'):
        mostrar_espectograma(snd)
    else:
        print('no puedo mostrar grafico')


def mostrar_grafico_ui(audio_seleccionado, grafico_seleccionado):
    snd = cargar_audio(audio_seleccionado)
    mostrar_grafico(grafico_seleccionado, snd)


if __name__ == '__main__':
    audio_entrada = input("Elije la ruta del audio:")
    senial = cargar_audio(audio_entrada)
    grafico_entrada = input(
        "Elije la salida (w = waveplot / e = espectograma):")
    mostrar_grafico(grafico_entrada, senial)
