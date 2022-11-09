import matplotlib.pyplot as plt
from scipy.io import wavfile


def cargar_audio(audio_seleccionado):
    muestra, senial = wavfile.read(audio_seleccionado)
    return muestra, senial
    

def mostrar_waveplot(audio_seleccionado):
    muestra, senial = cargar_audio(audio_seleccionado)
    plt.plot(senial)
    plt.ylabel('frequency [Hz]')
    plt.xlabel('time [s]')
    plt.show()


def mostrar_espectograma(audio_seleccionado):
    muestra, senial = cargar_audio(audio_seleccionado)
    plt.rcParams['axes.grid'] = False
    plt.specgram(senial, Fs=muestra, cmap='rainbow')
    plt.ylabel('frequency [Hz]')
    plt.xlabel('time [s]')
    plt.show()


def mostrar_grafico(grafico_seleccionado, audio_seleccionado):
    if grafico_seleccionado and (
            grafico_seleccionado.lower() == 'w'
            or grafico_seleccionado.lower() == 'waveplot'):
        mostrar_waveplot(audio_seleccionado)
    elif grafico_seleccionado and (
            grafico_seleccionado.lower() == 'e'
            or grafico_seleccionado.lower() == 'espectograma'):
            mostrar_espectograma(audio_seleccionado)
    else:
        print('no puedo mostrar grafico')


def mostrar_grafico_ui(audio_seleccionado, selected_plot):
    mostrar_grafico(selected_plot, audio_seleccionado)


if __name__ == '__main__':
    audio_entrada = input("Elije la ruta del audio:")
    grafico_entrada = input(
        "Elije la salida (w = waveplot / e = espectograma):")
    mostrar_grafico(grafico_entrada, audio_entrada)
   



