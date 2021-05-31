
import sys
import matplotlib.pyplot as plt
import parselmouth
import seaborn as sns
import numpy as np

sns.set()
plt.rcParams['figure.dpi'] = 100


def load_audio():
    selected_audio = input(
        "Elije el nombre del audio (debe estar en el folder audio):")
    try:
        return parselmouth.Sound("./audio/{0}.wav".format(selected_audio))
    except parselmouth.PraatError:
        sys.exit('Audio no encontrado')


def show_wave_plot(snd):
    plt.figure()
    plt.plot(snd.xs(), snd.values.T)
    plt.xlim([snd.xmin, snd.xmax])
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.show()


def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() -
                   dynamic_range, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")


def draw_intensity(intensity):
    plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("intensity [dB]")


def show_spectogram(snd):
    intensity = snd.to_intensity()
    spectrogram = snd.to_spectrogram()
    plt.figure()
    draw_spectrogram(spectrogram)
    plt.twinx()
    draw_intensity(intensity)
    plt.xlim([snd.xmin, snd.xmax])
    plt.show()


if __name__ == '__main__':
    snd = load_audio()
    select_plot = input("Elije la salida (w = waveplot / e = espectograma)")
    if select_plot == 'w':
        show_wave_plot(snd)
    if select_plot == 'e':
        show_spectogram(snd)
    else:
        print('no puedo mostrar grafico')
