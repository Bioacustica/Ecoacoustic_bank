import os
import hashlib
import datetime
import pandas as pd
import audio_metadata
import Globals
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

#https://www.altaruru.com/calculando-el-hash-en-python/

session = Session(engine)

def GetFingerprint(file):
    try:
        hashmd5 = hashlib.md5()
        with open(file, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashmd5.update(bloque)
        return hashmd5.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""

#AddRecordFile
def AddRecordFile(file, id_record):
    #crear directorio usando las primeras letras del fingerprint
    fingerprint = GetFingerprint(file)
    path_db = "/home/andres/Proyectos/Software/Bioacustico/DB/" + fingerprint[0:3]
    try:
        os.mkdir(path_db)
    except OSError:
        pass
    record_path = path_db + "/" + fingerprint + ".WAV"
    command = "cp " + file + " " + record_path
    os.system(command) 
    session.add(Base.classes["record_path"](id_record = id_record,
                                            record_path = record_path,
                                            fingerprint = fingerprint))
    session.flush()



def AddRecord(file, id_catalogue, date, chunk, session):
    
    metadata = audio_metadata.load(file)
    #try para format
    id_format = session.query(Base.classes["format"]). \
                filter(Base.classes["format"].description == os.path.splitext(file)[1].split('.')[1]).  \
                first().id_format
    
    Rec = Base.classes["record"](id_catalogue = id_catalogue,
                                 id_format = id_format,
                                 date = date,
                                 length = metadata['streaminfo'].duration,
                                 size = metadata.filesize,
                                 sample_rate = metadata['streaminfo'].sample_rate,
                                 chunk = chunk,
                                 channels = metadata['streaminfo'].channels)
    session.add(Rec)
    session.flush()
    id_record = session.query(Base.classes["record"]). \
                              filter(Base.classes["record"].id_record == Rec.id_record). \
                              first().id_record
    AddRecordFile(file = file,
                  id_record = id_record)
    #session.commit()


def AddRecords(file, id_catalogue, session):
    # catalogue: udas.iloc[i]["field_number_PR"]
    try:
        files = os.listdir(file)
        files.sort()
        # NOTA: la query para obtener el id_catalogue debe pulirse por que es posible 
        #       que dos catalogos tengan la misma descripción.
        
        for i in range(len(files)):
            
            date = datetime.datetime(year = int(files[i][0:4]),
                                     month = int(files[i][4:6]),
                                     day = int(files[i][6:8]),
                                     hour = int(files[i][9:11]),
                                     minute = int(files[i][11:13]),
                                     second = int(files[i][13:15]))
            
            AddRecord(file = os.path.join(file,files[i]),
                      id_catalogue = id_catalogue,
                      date = date,
                      chunk = i,
                      session = session)
    except:
        pass



def AddRecords_(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for id in range(udas.shape[0]):
        try:
            catalogue = udas.iloc[id]["field_number_PR"]
            id_catalogue = session.query(Base.classes["catalogue"]). \
                           filter(Base.classes["catalogue"].description == catalogue). \
                           first().id_catalogue
            
            file = udas.iloc[id]["path_records_PR"]
            AddRecords(file, id_catalogue, session)
        except:
            Globals.Bug = True
            if not 'id_catalogue' in locals():
                print("  ERROR: field_number_PR - " + str(id + 2) + " ->  " + str(catalogue))
            elif file != file:
                print("  ERROR: path_records_PR - " + str(id + 2) + " ->  " + str(file))




#AddRecords(file = "/home/andres/Proyectos/Software/Bioacustico/G1",
#           catalogue = 'G1', 
#           session = session)
