import zlib

from django.conf import settings
import psycopg2
import json
import jwt
import base64
import time
from django.http import StreamingHttpResponse

from cryptography.fernet import Fernet


def choose_role(username: str, password: str, roles: str) -> str:
    """Función encargada de crear roles con el usuario y contraseña

    :param username: nombre del usuario
    :type username: str
    :param password: contraseña del usuario
    :type password: str
    :param roles:  rol que se le asiganará al usuario
    :type roles: str
    :return:  devuelve el query que será ejecutado por un cursor en postgres
    :rtype: str
    """
    rol = roles

    roles = {
        "admin": "SELECT bioacustica.create_user_admin('{}','{}')".format(
            username, password
        ),
        "registro": "SELECT bioacustica.create_user_registros('{}','{}')".format(
            username, password
        ),
        "etiquetado": "SELECT bioacustica.create_user_etiquetado('{}','{}')".format(
            username, password
        ),
        "usuario": "SELECT bioacustica.create_user_usuario('{}','{}')".format(
            username, password
        ),
    }

    return roles[rol]


def change_password(username: str, password: str) -> str:
    """
    :param username: recibe el nombre de usuario
    :param password: recibe la contraseña de usuario
    :return: devuelve un query que será ejecutado por un cursor en postgres
    """
    query = "SELECT bioacustica.change_password('{}', '{}')".format(username, password)
    return query


def delete_user(username: str) -> str:
    """
    Función encargada de eliminar usuarios de la entidad users
    y del postgres
    :param username:
    :return: query que será ejecutado por un cursor
    """
    query = "SELECT bioacustica.drop_user('{}')".format(username)
    return query


def consulta_filtros(
    token: str,
    catalogo=None,
    habitat=None,
    municipio=None,
    evento=None,
    tipo_case=None,
    tipo_micro=None,
    metodo_etiquetado=None,
    software=None,
    tipo_grabadora=None,
) -> list:
    """
    Esta función  tiene 2 partes la primera es la extracción del nombre y el password del token
    la segunda es la creación de una consulta  a la bd que se hará con las credenciales extraidas
    se hace una consulta externa a la django ya que a nivel de bases de datos se están usando
    permisos personalizados


    :param catalogo:
    :param habitat:
    :param municipio:
    :param evento:
    :param tipo_case:
    :param tipo_micro:
    :param metodo_etiquetado:
    :param software:
    :param tipo_grabadora:
    :param token: es un str donde están codificada información de interés
    :return: retorna una lista de diccionarios
    """

    # 1ra parte se hace la decodficación del token y se almacenan las variables de interés
    decoded = jwt.decode(token[7:], options={"verify_signature": False})
    pwd = decoded["password"].encode()
    nombre_usuario = decoded["user"]
    # se crea una conexión usando las credenciales del superuser  y se hace la consulta de la tabla de interés
    credenciales_db_admin = {
        "user": "animalesitm",
        "password": "animalesitm",
        "host": "postgres",
        "port": 5432,
        "database": "animalesitm",
    }
    conexion1 = psycopg2.connect(**credenciales_db_admin)
    conexion1.autocommit = True
    key_query = "SELECT key FROM bioacustica.keys where username='{}';".format(
        nombre_usuario
    )
    # se extrae la información necesaria
    with conexion1.cursor() as cursor1:
        cursor1.execute(key_query)
        raw = cursor1.fetchone()
        raw_str = str(raw[0]).encode()

    with open("keys.json") as f:
        data = json.load(f)

    username = data["username"]
    key = data["key"].encode()
    # 2da parte
    # se crea la desencriptación y se crea la conexión con el usuario de interés
    fernet = Fernet(raw_str)
    raw_password = fernet.decrypt(pwd).decode()
    db_name = settings.DATABASES["animalesitm"]["NAME"]
    db_port = settings.DATABASES["animalesitm"]["PORT"]
    db_host = settings.DATABASES["animalesitm"]["HOST"]
    credenciales_db = {
        "user": nombre_usuario,
        "password": raw_password,
        "host": db_host,
        "port": db_port,
        "database": db_name,
    }
    # se hace la consulta y se crea el objecto con los datos consultados
    print(type(catalogo))
    print(habitat)
    print(municipio)
    print(evento)
    print(tipo_case)
    print(tipo_micro)
    print(metodo_etiquetado)
    print(software)
    print(tipo_grabadora)
    conexion2 = psycopg2.connect(**credenciales_db)
    query = "SELECT * FROM bioacustica.get_join ({0},{1},{2},{3},{4},{5},{6},{7},{8});".format(

            catalogo,
            habitat,
            municipio,
            evento,
            tipo_case,
            tipo_micro,
            metodo_etiquetado,
            software,
            tipo_grabadora

    )
    with conexion2.cursor() as cursor2:
        cursor2.execute(query)
        fetch = cursor2.fetchall()
        objects_list = []
        column_names = [column[0] for column in cursor2.description]
        for record in fetch:
            objects_list.append(dict(zip(column_names, record)))
    return objects_list


def base_64_encoding(file_path: str) -> bytes:
    """
    Función encargada de convertir a base64
    archivos de audio con extensión .wav

    :param file_path:  recibe los diccionarios donde se ecuentran los paths
    :return: retorna el contenido del base 64
    """
    # converted = AudioSegment.from_mp3(file_path)
    # converted.export("converted.wav", format="wav")
    file = open(file_path, "rb")
    audio_content = file.read()
    b64_content = base64.b64encode(audio_content)
    return b64_content


def read_file(filename, buf_size=1000000):
    with open(filename, "rb") as f:
        while True:
            content = f.read(buf_size)
            if content:
                yield content
            else:
                break
