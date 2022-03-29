import os
import datetime
import pandas as pd
import audio_metadata
from mapping import Bug
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session


session = Session(engine)


def AddRecord(file, id_catalogue, date, chunk, session):
    
    metadata = audio_metadata.load(file)
    
    id_format = session.query(Base.classes["format"]). \
                filter(Base.classes["format"].description == os.path.splitext(file)[1].split('.')[1]).  \
                first().id_format
    
    session.add(Base.classes["record"](id_catalogue = id_catalogue,
                                       id_format = id_format,
                                       date = date,
                                       length = metadata['streaminfo'].duration,
                                       size = metadata.filesize,
                                       sample_rate = metadata['streaminfo'].sample_rate,
                                       chunk = chunk,
                                       channels = metadata['streaminfo'].channels))
    session.commit()


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
            Bug = True
            if file != file:
                print("ERROR: path_records_PR - " + str(id+1) + " ->  " + str(file))
            elif not 'id_catalogue' in locals():
                print("ERROR: field_number_PR - " + str(id+1) + " ->  " + str(catalogue))




#AddRecords(file = "/home/andres/Proyectos/Software/Bioacustico/G1",
#           catalogue = 'G1', 
#           session = session)
