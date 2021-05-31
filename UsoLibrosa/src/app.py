
import sys
import matplotlib.pyplot as plt
import librosa.display
import librosa


def load_audio():
    selected_audio = input(
        "Elije el nombre del audio (debe estar en el folder audio):")
    try:
        return librosa.load("./audio/{0}.wav".format(selected_audio))
    except FileNotFoundError:
        sys.exit('Audio no encontrado')


def show_wave_plot(y, sr):
    plt.figure(figsize=(14, 5))
    # plotting the sampled signal
    librosa.display.waveplot(y, sr=sr)
    plt.show()


def show_spectogram(y, sr):
    # x: numpy array
    numpy_arr = librosa.stft(y)
    # converting into energy levels(dB)
    energy_lvl = librosa.amplitude_to_db(abs(numpy_arr))

    plt.figure(figsize=(20, 5))
    librosa.display.specshow(energy_lvl, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    y, sr = load_audio()
    select_plot = input("Elije la salida (w = waveplot / e = espectograma)")
    if select_plot == 'w':
        show_wave_plot(y, sr)
    if select_plot == 'e':
        show_spectogram(y, sr)
    else:
        print('no puedo mostrar grafico')
