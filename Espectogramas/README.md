# bioacustica

# Iniciar

## Sin Docker

Instalar python3 tkinter for UI:
sudo apt install python3-tk
Instalar pipenv:
pip3 install pipenv
Luego, crear el folder para alojar el entorno virtual:
mkdir .venv
Lanzar pipenv:
pipenv install --skip-lock
Activar virtual env:
pipenv shell
Correr comandos en el virtualenv:
pipenv run
Salir de virtualenv:
exit o deactivate

## Con Docker

docker build -t bioacustica .
docker run --rm -it bioacustica pipenv shell
python3 src/librosa_util.py

# Configurar

Configurar todas las dependencias en el Pipfile.
Ver: https://pypi.org/

# Ejecutar

## Modo Grafico

python3 src/ui.py

## Modo consola

python3 src/librosa_util.py
python3 src/praat_util.py
python3 src/scipy_util.py

# Referencias

https://soundbible.com/
https://parselmouth.readthedocs.io/en/stable/
https://librosa.org/doc/latest/tutorial.html
