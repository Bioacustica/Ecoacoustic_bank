import os
import datetime
import pandas as pd
from mapping import Bug
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def AddCatalogue(udas, session, id):
    
    try:
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
                    filter(Base.classes["supply"].description == udas.iloc[id]["power_source_RE"].replace('"','').upper()). \
                    first().id_supply
        
        id_case = session.query(Base.classes["case"]). \
                  filter(Base.classes["case"].description == udas.iloc[id]["rec_case_RE"].replace('"','').upper()). \
                  first().id_case
        
        id_memory = session.query(Base.classes["memory"]). \
                    filter(Base.classes["memory"].description == udas.iloc[id]["memory_card_RE"].replace('"','').upper()). \
                    first().id_memory
        
        id_habitat = session.query(Base.classes["habitat"]). \
                     filter(Base.classes["habitat"].description == udas.iloc[id]["habitat_HA"].replace('"','').upper()). \
                     first().id_habitat
        
        id_precision = session.query(Base.classes["precision"]). \
                       filter(Base.classes["precision"].description == udas.iloc[id]["precision_IG"].replace('"','').upper()). \
                       first().id_precision
        
        id_datum = session.query(Base.classes["datum"]). \
                   filter(Base.classes["datum"].description == udas.iloc[id]["datum_IG"].replace('"','').upper()).  \
                   first().id_datum
        
        id_microphone = session.query(Base.classes["microphone"]). \
                        filter(Base.classes["microphone"].description == udas.iloc[id]["microphone_RE"].replace('"','').upper()). \
                        first().id_microphone
        
        elevation = udas.iloc[id]["min_elevation_IG"]
        height = udas.iloc[id]["rec_height_HA"]
        latitude = udas.iloc[id]["latitude_IG"]
        longitude = udas.iloc[id]["longitud_IG"]
        description = udas.iloc[id]["field_number_PR"]
        record_dir = udas.iloc[id]["path_records_PR"]

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
    except:
        Bug = True
        if not 'id_sampling' in locals():
            print("ERROR: id_DM - " + str(id + 2) + " ->  " + str(udas.iloc[id]["id_DM"]) )
        elif not 'id_country' in locals():
            print("ERROR: country_IG - " + str(id + 2) + " ->  " + str(udas.iloc[id]["country_IG"]) )
        elif not 'id_department' in locals():
            print("ERROR: department_IG - " + str(id + 2) + " ->  " + str(udas.iloc[id]["department_IG"]) ) 
        elif not 'id_m' in locals():
            print("ERROR: municipality_IG - " + str(id + 2) + " ->  " + str(udas.iloc[id]["municipality_IG"]) )
        elif not 'id_vereda' in locals():
            print("ERROR: id_vereda - " + str(id + 2) + " ->  " + str(udas.iloc[id]["id_vereda"]) )
        elif not 'id_locality' in locals():
            print("ERROR: id_locality - " + str(id + 2) + " ->  " + str(udas.iloc[id]["id_locality"]) )
        elif not 'id_gain' in locals():
            print("ERROR: gain_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["gain_RE"]) ) 
        elif not 'id_filter' in locals():
            print("ERROR: filters_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["filters_RE"]) )
        elif not 'id_collector' in locals():
            print("ERROR: collector_email_PR - " + str(id + 2) + " ->  " + str(udas.iloc[id]["collector_email_PR"]) )
        elif not 'id_h_serial' in locals():
            print("ERROR: rec_serial_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["rec_serial_RE"]) )
        elif not 'id_supply' in locals():
            print("ERROR: power_source_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["power_source_RE"]) ) 
        elif not 'id_case' in locals():
            print("ERROR: rec_case_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["rec_case_RE"]) )
        elif not 'id_memory' in locals():
            print("ERROR: memory_card_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["memory_card_RE"]) )
        elif not 'id_habitat' in locals():
            print("ERROR: habitat_HA - " + str(id + 2) + " ->  " + str(udas.iloc[id]["habitat_HA"]) )
        elif not 'id_precision' in locals():
            print("ERROR: precision_IG - " + str(id + 2) + " ->  " + str(udas.iloc[id]["precision_IG"]) ) 
        elif not 'id_datum' in locals():
            print("ERROR: datum_IG - " + str(id + 2) + " ->  " + str(udas.iloc[id]["datum_IG"]) )
        elif not 'id_microphone' in locals():
            print("ERROR: microphone_RE - " + str(id + 2) + " ->  " + str(udas.iloc[id]["microphone_RE"]) )
          

def AddCatalogues_(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for id in range(udas.shape[0]):
        
        AddCatalogue(udas, session, id)







#id_catalogue = session.query(Base.classes["catalogue"]). \
#               filter(Base.classes["catalogue"].description == udas.iloc[i]["catalogue"]). \
#               first().id_catalogue

#RecordsAdd(file = udas.iloc[i]["record"],
#            id_catalogue = id_catalogue,
#            session = session)

        



#AddCatalogues_(file = "UDAS_20210406.xls", session = session)
