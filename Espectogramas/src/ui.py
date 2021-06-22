from tkinter import Tk, Frame, Button, Label,  ttk, messagebox
from tkinter.filedialog import askopenfilename
from librosa_util import mostrar_grafico_ui as librosa_mostrar_grafico_ui
from praat_util import mostrar_grafico_ui as praat_mostrar_grafico_ui
from scipy_util import mostrar_grafico_ui as scipy_mostrar_grafico_ui


def validar_entrada(arg_entrada, valor_defecto):
    if arg_entrada == "" or arg_entrada.strip() == "":
        return valor_defecto
    else:
        return arg_entrada


def cargar_archivo():
    archivo_seleccionado = askopenfilename(filetypes=(
        ('audios', '*.wav'), ('todos', '*.*')))
    msj_label.config(text=archivo_seleccionado)


def ejecutar_util():
    grafico_seleccionado = validar_entrada(
        graficos_opciones_dd.get(), "Espectograma")
    fmw_seleccionado = validar_entrada(fmw_opciones_dd.get(), "Librosa")
    archivo_seleccionado = msj_label.cget('text')
    if fmw_seleccionado == 'Librosa':
        librosa_mostrar_grafico_ui(archivo_seleccionado, grafico_seleccionado)
    elif fmw_seleccionado == 'Praat':
        praat_mostrar_grafico_ui(archivo_seleccionado, grafico_seleccionado)
    elif fmw_seleccionado == 'Scipy':
        scipy_mostrar_grafico_ui(archivo_seleccionado, grafico_seleccionado)
    else:
        messagebox.showerror('Bioacustica App - Error',
                             'Debe seleccionar Librosa o Praat')


principal = Tk()
principal.title('Bioacustica - Analisis de audio')

ventana_1 = Frame(principal)
ventana_1.pack()

fmw_opciones = ['Librosa', 'Praat', 'Scipy']
fmw_opciones_dd = ttk.Combobox(
    ventana_1, width=15, state='readonly', values=fmw_opciones)
fmw_opciones_dd.grid(row=1, column=1, padx=10, pady=10)
fmw_opciones_dd.current(0)
graficos_opciones = ['Espectograma', 'Waveplot']
graficos_opciones_dd = ttk.Combobox(
    ventana_1, width=15, state='readonly', values=graficos_opciones)
graficos_opciones_dd.grid(row=2, column=1, padx=10, pady=10)
graficos_opciones_dd.current(0)
cargar_boton = Button(ventana_1, text="Cargar archivo",
                      width="15", height="1", command=cargar_archivo)
cargar_boton.grid(row=3, column=1, padx=10, pady=10)
msj_label = Label(ventana_1, text="")
msj_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)
generar_boton = Button(ventana_1, text="Generar Grafico",
                       width="15", height="1", command=ejecutar_util)
generar_boton.grid(row=5, column=1, padx=10, pady=10)
principal.mainloop()
