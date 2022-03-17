import pandas as pd
from mapping import Base
from mapping import engine


def LoadMasterTable(mapping, info_path, table_name, engine, schema):
    # mapping: sqlalchemy.ext.automap (Base.classes)
    # info_path: string with file path ('MasterTables.xls')
    # table_name: string with table name ('evidence')
    # engine: database conection
    # schema: ('bioacustica')
    columns_names = mapping[table_name].__table__.columns.keys()
    tableToLoad = pd.read_excel(info_path, sheet_name = table_name, header = None)
    tableToLoad = tableToLoad.applymap(lambda x: x.replace('"','').upper())
    tableToLoad.columns = [columns_names[1]]
    tableToLoad[columns_names[0]] = range(1,tableToLoad.shape[0]+1)
    tableToLoad = tableToLoad.reindex(columns = columns_names)

    for i in range(len(tableToLoad)):
        try:
            tableToLoad.iloc[i:i+1].to_sql(name = table_name, con = engine, schema = 'bioacustica', if_exists = 'append', index = False)
        except:
            pass




sheets = pd.ExcelFile('/home/andres/Proyectos/Software/Bioacustico/bioacustica/MasterTables.xls').sheet_names

for sheet in sheets:
    try:
        LoadMasterTable(mapping = Base.classes,
                        info_path = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/MasterTables.xls',
                        table_name = sheet,
                        engine = engine,
                        schema = 'bioacustica')
    except:
        print("Error",sheet)

#----------------------------------

from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

session.add(Base.classes["user"](name = "JUAN MANUEL",
                                 email = "juanm.daza@udea.edu.co",
                                 username = "juanm.daza",
                                 roles = "ADMINISTRADOR"))
session.commit()


#----------------------------------

from sqlalchemy.orm import Session

session = Session(engine)

id_funding = session.query(Base.classes["funding"]).filter(Base.classes["funding"].description == 'GHA').first().id_funding
session.add(Base.classes["project"](id_funding = id_funding,
                                    description = "Proyecto Piloto YNC",))
session.commit()

#---------------------------------

import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

def ProjectAdd(udas, session, id):

    id_funding = session.query(Base.classes["funding"]).filter(Base.classes["funding"].description == udas.iloc[0]["funding_PR"]).first().id_funding
    
    session.add(Base.classes["project"](id_funding = id_funding,
                                        description = udas.iloc[id]["project_name_PR"]))


def ProjectsAdd(file, session, id):

    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for i in range(udas.shape[0]):

        ProjectAdd(udas, session, id)


#----------------------------------

import datetime
import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def SamplingAdd(udas, session, id):
    
    id_season = session.query(Base.classes["season"]).filter(Base.classes["season"].description == udas.iloc[id]["season_HA"]).first().id_season
    id_project = session.query(Base.classes["project"]).filter(Base.classes["project"].description == udas.iloc[id]["project_name_PR"]).first().id_project
    id_cataloger = session.query(Base.classes["user"]).filter(Base.classes["user"].email == udas.iloc[id]["collector_email_PR"]).first().id_user
    
    session.add(Base.classes["sampling"](id_project = id_project,
                                         id_cataloger = id_cataloger,
                                         id_season = id_season,
                                         date = datetime.datetime.now(),
                                         description = udas.iloc[id]["id_DM"]))
    session.commit()


def SamplingsAdd(file, session, id):

    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)

    for i in range(udas.shape[0]):

        SamplingAdd(udas, session, id)


SamplingsAdd(file = "../UDAS_20210406.xls", session = session, id = 0)

#----------------------------------
import os
import datetime
import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def CatalogueAdd(file, session, id):
    
    udas = pd.read_excel(file, sheet_name = "Template", header = 0)
    record_dir = udas.iloc[id]["record"]
    infoDir = os.listdir(record_dir)
    
    id_sampling = session.query(Base.classes["sampling"]). \
                  filter(Base.classes["sampling"].description == udas.iloc[id]["sampling"]). \
                  first().id_sampling
    
    id_country =  session.query(Base.classes["country"]). \
                  filter(Base.classes["country"].description == udas.iloc[id]["country"].replace('"','').upper()). \
                  first().id_country
    
    id_department = session.query(Base.classes["department"]). \
                    filter(Base.classes["department"].description == udas.iloc[id]["department"].replace('"','').upper()). \
                    first().id_department
    
    id_m = session.query(Base.classes["municipality"]). \
           filter(Base.classes["municipality"].description == udas.iloc[id]["municipality"].replace('"','').upper()). \
           first().id_municipality
    
    id_vereda = 1
    id_locality = 1
    
    id_gain = session.query(Base.classes["gain"]). \
              filter(Base.classes["gain"].description == udas.iloc[id]["gain"].replace('"','').upper()). \
              first().id_gain
    
    #id_filter = session.query(Base.classes["filter"]). \
    #          filter(Base.classes["filter"].description == udas.iloc[id]["filter"].replace('"','').upper()). \
    #          first().id_filter
    id_filter = 1
    
    id_collector = session.query(Base.classes["user"]).filter(Base.classes["user"].email == udas.iloc[id]["collector"]).first().id_user
    id_h_serial = 1
    
    id_supply = session.query(Base.classes["supply"]). \
                filter(Base.classes["supply"].description == udas.iloc[id]["supply"].replace('"','').upper()). \
                first().id_supply
    
    id_case = session.query(Base.classes["case"]). \
              filter(Base.classes["case"].description == udas.iloc[id]["case"].replace('"','').upper()). \
              first().id_case
    
    id_memory = session.query(Base.classes["memory"]). \
                filter(Base.classes["memory"].description == udas.iloc[id]["memory"].replace('"','').upper()). \
                first().id_memory
    
    id_habitat = session.query(Base.classes["habitat"]). \
                 filter(Base.classes["habitat"].description == udas.iloc[id]["habitat"].replace('"','').upper()). \
                 first().id_habitat
    
    id_precision = session.query(Base.classes["precision"]). \
                   filter(Base.classes["precision"].description == udas.iloc[id]["precision"].replace('"','').upper()). \
                   first().id_precision
    
    id_datum = session.query(Base.classes["datum"]). \
               filter(Base.classes["datum"].description == udas.iloc[id]["datum"].replace('"','').upper()).  \
               first().id_datum
    
    id_microphone = session.query(Base.classes["microphone"]). \
                    filter(Base.classes["microphone"].description == udas.iloc[id]["microphone"].replace('"','').upper()). \
                    first().id_microphone
    
    elevation = udas.iloc[id]["elevation"]
    height = udas.iloc[id]["height"]
    chunks = len(infoDir)
    size = 1
    latitude = udas.iloc[id]["latitude"]
    longitude = udas.iloc[id]["longitude"]
    description = udas.iloc[id]["catalogue"]
    
    session.add(Base.classes["catalogue"](id_sampling = id_sampling,
                                          id_country = id_country,
                                          id_department = id_department,
                                          id_municipality = id_m, 
                                          id_vereda = id_vereda, 
                                          id_locality = id_locality,
                                          id_gain = id_gain, 
                                          id_filter = id_filter,
                                          id_collector = id_collector,
                                          id_h_serial = id_h_serial,
                                          id_supply = id_supply,
                                          id_case = id_case,
                                          id_memory = id_memory,
                                          id_habitat = 1,
                                          id_precision = id_precision,
                                          id_datum = id_datum,
                                          id_microphone = id_microphone,
                                          elevation = elevation.tolist(), 
                                          height = height.tolist(),
                                          chunks = chunks,
                                          size = pd.to_numeric(size, downcast = 'float'),
                                          latitude = pd.to_numeric(latitude, downcast = 'float'),
                                          longitude = pd.to_numeric(longitude, downcast = 'float'),
                                          description = description))
    session.commit()


CatalogueAdd(file = "../UDAS_20210406.xls", session = session, id = 1)

def CataloguesAdd(file, session):
    
    udas = pd.read_excel(file, sheet_name = "Template", header = 0)
    
    for i in range(udas.shape[0]):
        
        id_sampling = 0
        id_sampling = session.query(Base.classes["sampling"]). \
                      filter(Base.classes["sampling"].description == udas.iloc[i]["sampling"]). \
                      first().id_sampling
        
        # Si el sampling no esta creado lo crea
        if id_sampling == 0:
            
            SamplingAdd(file = file, session = session, id = i)
            id_sampling = session.query(Base.classes["sampling"]). \
                      filter(Base.classes["sampling"].description == udas.iloc[i]["sampling"]). \
                      first().id_sampling
        
        CatalogueAdd(file = file,
                     session = session,
                     id = i)
        
        id_catalogue = session.query(Base.classes["catalogue"]). \
                       filter(Base.classes["catalogue"].description == udas.iloc[i]["catalogue"]). \
                       first().id_catalogue
        
        RecordsAdd(file = udas.iloc[i]["record"],
                   id_catalogue = id_catalogue,
                   session = session)

        



CataloguesAdd(file = "UDAS_20210406.xls", session = session)

#----------------------------------

import os
import datetime
import pandas as pd
import audio_metadata
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session


session = Session(engine)


def RecordAdd(file, id_catalogue, date, chunk, session):
    
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




def RecordsAdd(file, id_catalogue, session):
    
    files = os.listdir(file)
    files.sort()
    
    for i in range(len(files)):
        
        date = datetime.datetime(year = int(files[i][0:4]),
                                month = int(files[i][4:6]),
                                day = int(files[i][6:8]),
                                hour = int(files[i][9:11]),
                                minute = int(files[i][11:13]),
                                second = int(files[i][13:15]))
        
        RecordAdd(file = os.path.join(file,files[i]),
                  id_catalogue = id_catalogue,
                  date = date,
                  chunk = i,
                  session = session)


RecordsAdd(file = "/home/andres/Proyectos/Software/Bioacustico/G1", id_catalogue = 4, session = session)

#----------------------------------

# Temas a discutir
# 1) Dependencia entre project y funding
# 2) Coherencia entre la información de las tablas maestras y la plantilla (tocaria agregar mas información a las tablas maestras o editarlas?)
# 3) Como referenciar al usuario (por email, nombre o username)
# 4) Hablar de la plantilla (separar por hojas (sampling, catalogo y registro)) es un UDAS por sampling
# 5) Nombre del sampling (nombre del estudio) iria en description
