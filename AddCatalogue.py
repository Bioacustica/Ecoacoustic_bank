import os
import datetime
import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def AddCatalogue(udas, session, id):
    
    id_sampling = session.query(Base.classes["sampling"]). \
                  filter(Base.classes["sampling"].description == udas.iloc[id]["id_DM"]). \
                  first().id_sampling
    
    id_country =  session.query(Base.classes["country"]). \
                  filter(Base.classes["country"].description == udas.iloc[id]["country_IG"].replace('"','').upper()). \
                  first().id_country
    
    id_department = session.query(Base.classes["department"]). \
                    filter(Base.classes["department"].description == udas.iloc[id]["department_IG"].replace('"','').upper()). \
                    first().id_department
    
    id_m = session.query(Base.classes["municipality"]). \
           filter(Base.classes["municipality"].description == udas.iloc[id]["municipality_IG"].replace('"','').upper()). \
           first().id_municipality
    
    id_vereda = 1
    id_locality = 1
    
    id_gain = session.query(Base.classes["gain"]). \
              filter(Base.classes["gain"].description == udas.iloc[id]["gain_RE"].replace('"','').upper()). \
              first().id_gain
    
    #id_filter = session.query(Base.classes["filter"]). \
    #          filter(Base.classes["filter"].description == udas.iloc[id]["filter"].replace('"','').upper()). \
    #          first().id_filter
    id_filter = 1
    
    id_collector = session.query(Base.classes["user"]).filter(Base.classes["user"].email == udas.iloc[id]["collector_email_PR"]).first().id_user
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
    latitude = udas.iloc[id]["latitude"]
    longitude = udas.iloc[id]["longitude"]
    description = udas.iloc[id]["catalogue"]
    record_dir = udas.iloc[id]["record"]

    infoDir = os.listdir(record_dir)
    chunks = len(infoDir)
    size = 1
    
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
                                          id_habitat = id_habitat,
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


#CatalogueAdd(file = "../UDAS_20210406.xls", session = session, id = 1)

def AddCatalogues(file, session):
    
    udas = pd.read_excel(file, sheet_name = "Template", header = 0)
    
    for i in range(udas.shape[0]):
        
        id_sampling = 0
        id_sampling = session.query(Base.classes["sampling"]). \
                      filter(Base.classes["sampling"].description == udas.iloc[i]["sampling"]). \
                      first().id_sampling
        
        # Si el sampling no esta creado lo crea
        if id_sampling == 0:
            
            AddSampling(file = file, session = session, id = i)
            id_sampling = session.query(Base.classes["sampling"]). \
                      filter(Base.classes["sampling"].description == udas.iloc[i]["sampling"]). \
                      first().id_sampling
        
        AddCatalogue(file = file,
                     session = session,
                     id = i)
        
        id_catalogue = session.query(Base.classes["catalogue"]). \
                       filter(Base.classes["catalogue"].description == udas.iloc[i]["catalogue"]). \
                       first().id_catalogue
        
        RecordsAdd(file = udas.iloc[i]["record"],
                   id_catalogue = id_catalogue,
                   session = session)

        



CataloguesAdd(file = "UDAS_20210406.xls", session = session)
