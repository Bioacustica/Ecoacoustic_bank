import os
import re
import hashlib
import datetime
import pandas as pd
import audio_metadata
from . import Globals
from .Globals import VerifyField
from .mapping import Base
from .mapping import engine
from sqlalchemy.orm import Session
import subprocess

# https://www.altaruru.com/calculando-el-hash-en-python/

session = Session(engine)

def PrefixRemover(texto, caracter = "_"):
    # Elimina todos los caracteres que están antes del primer guion bajo en el texto.
    
    if texto.count(caracter) < 2:
        return texto
    
    index = texto.find(caracter)
    
    return texto[(index+1):]


def IsNewRecord(fingerprint):
    Record = (
        session.query(Base.classes["record_path"])
        .filter(Base.classes["record_path"].fingerprint == fingerprint)
        .first()
    )
    return Record == None


def GetFingerprint(file):
    try:
        return hashlib.md5(open(file, "rb").read()).hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""

# AddRecordFile


def AddRecordFile(file, fingerprint, id_record):

    #path_db = "/share/Audios_DB/audios_db/" + fingerprint[0:3]
    path_db = "/code/audios_db/" + fingerprint[0:3]

    try:
        os.mkdir(path_db)
    except Exception as e:
        pass
    try:
        record_path = path_db + "/" + fingerprint + ".WAV"
        command = "cp " + file + " " + record_path  # + " &"
        print("  Adding " + file[-19:])
        # command = "sleep 60"
        subprocess.run(command, shell=True)
        # print(status)
        # os.system(command)
        RecPath = Base.classes["record_path"](id_record=id_record,
                                              record_path=record_path,
                                              fingerprint=fingerprint)
        session.add(RecPath)
        session.flush()
        session.commit()
    except Exception as e:
        print("6")
        print(e)
        Globals.Bug = True


def AddRecord(file, id_catalogue, date, chunk, session):
    metadata = audio_metadata.load(file)
    # try para format
    format = os.path.splitext(file)[1].split('.')[1].upper()

    id_format = session.query(Base.classes["format"]). \
        filter(Base.classes["format"].description == format).  \
        first().id_format

    Rec = Base.classes["record"](id_catalogue=id_catalogue,
                                 id_format=id_format,
                                 date=date,
                                 length=metadata['streaminfo'].duration,
                                 size=metadata.filesize,
                                 sample_rate=metadata['streaminfo'].sample_rate,
                                 chunk=chunk,
                                 channels=metadata['streaminfo'].channels)

    fingerprint = GetFingerprint(file)
    if IsNewRecord(fingerprint):

        session.add(Rec)
        session.flush()
        session.commit()
        # print(file)
        id_record = session.query(Base.classes["record"]). \
            filter(Base.classes["record"].id_record == Rec.id_record). \
            first().id_record
        AddRecordFile(file=file,
                      fingerprint=fingerprint,
                      id_record=id_record)
    else:
        Globals.Bug = True
        print(" ERROR:  Record " + str(fingerprint) + " already exists")


def AddRecords(file, id_catalogue, session):
    # catalogue: udas.iloc[i]["field_number_PR"]
    try:

        files = os.listdir(file)

        # Quitar archivos ocultos (aquellos archivos que empiecen con punto)
        files = [elemento for elemento in files if not elemento.startswith('.')]
        files.sort()

        for i in range(len(files)):

            # Quitar prefijo
            file_ = PrefixRemover(files[i])

            date = datetime.datetime(
                year = int(file_[0:4]),
                month = int(file_[4:6]),
                day = int(file_[6:8]),
                hour = int(file_[9:11]),
                minute = int(file_[11:13]),
                second = int(file_[13:15]),
            )

            AddRecord(
                file = os.path.join(file, file_),
                id_catalogue = id_catalogue,
                date = date,
                chunk = i,
                session = session,
            )

    except Exception as e:
        print("5")
        raise print(e)


def AddRecords_(file, session, path_usb):

    udas = pd.read_excel(file, sheet_name="UDAS", header=0)

    for id in range(udas.shape[0]):
        try:

            Ok = True

            project = udas.iloc[id]["project_name_PR"]
            Ok = VerifyField("project_name_PR", project, id) and Ok

            sampling = udas.iloc[id]["id_DM"]
            Ok = VerifyField("id_DM", sampling, id) and Ok

            catalogue = udas.iloc[id]["field_number_PR"]
            Ok = VerifyField("field_number_PR", catalogue, id) and Ok

            file = udas.iloc[id]["path_records_PR"]
            Ok = VerifyField("path_records_PR", file, id) and Ok
            file = path_usb + file + "/" + catalogue

            if not Ok:
                raise

            id_project = (
                session.query(Base.classes["project"])
                .filter(Base.classes["project"].description == project)
                .first()
                .id_project
            )

            id_sampling = (
                session.query(Base.classes["sampling"])
                .filter(Base.classes["sampling"].id_project == id_project)
                .filter(Base.classes["sampling"].description == sampling)
                .first()
                .id_sampling
            )

            id_catalogue = (
                session.query(Base.classes["catalogue"])
                .filter(Base.classes["catalogue"].id_sampling == id_sampling)
                .filter(Base.classes["catalogue"].description == catalogue)
                .first()
                .id_catalogue
            )

            AddRecords(file, id_catalogue, session)
        except Exception as e:
            Globals.Bug = True
            print("4")
            print(e)
            if not "id_catalogue" in locals():
                # el catalogo no fue creado
                print(
                    "  ERROR: field_number_PR - "
                    + str(id + 2)
                    + " ->  "
                    + str(catalogue)
                )
            elif file != file:
                print("  ERROR: path_records_PR - " +
                      str(id + 2) + " ->  " + str(file))


# AddRecords(file = "/home/andres/Proyectos/Software/Bioacustico/G1",
#           catalogue = 'G1',
#           session = session)
