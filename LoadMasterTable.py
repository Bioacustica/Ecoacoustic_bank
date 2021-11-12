#!/usr/bin/env python3

print("\n\n\nESTE ARCHIVO DE PYTHON SE ESTÁ CORRIENDO DESDE UN BASH EN DOCKER!!\n\n\n")

from datetime import datetime
import random

import pandas as pd
# from sqlalchemy.sql.elements import Label
# import xlsxwriter
from sqlalchemy.orm import Session  # , load_only
from sqlalchemy import MetaData

from mapping import Base
from mapping import engine

session = Session(engine)

# TODO: Documentar en el readme la carga de datos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def load_master_table(mapping, info_path, table_name, engine, schema):
    # mapping: sqlalchemy.ext.automap (Base.classes)
    # info_path: string with file path ('MasterTables.xls')
    # table_name: string with table name ('evidence')
    # engine: database conection
    # schema: ('bioacustica')
    columns_names = mapping[table_name].__table__.columns.keys()
    tableToLoad = pd.read_excel(info_path, sheet_name = table_name, header = None)
    tableToLoad = tableToLoad.applymap(lambda x: preprocess(x))
    tableToLoad.columns = [columns_names[1]]
    tableToLoad[columns_names[0]] = range(1,tableToLoad.shape[0]+1)
    tableToLoad = tableToLoad.reindex(columns = columns_names)
    tableToLoad.to_sql(name = table_name, schema ='bioacustica', index = False, con = engine, if_exists = 'append')


def preprocess(x):
    if type(x) is str:
       x = x.replace('"','').upper()
    return x


def load_second_table(mapping, info_path, table_name, engine, schema):
    """Esta funcion servirá para la carga de las plantillas con los IDs a futuro

    :param mapping: [description]
    :type mapping: [type]
    :param info_path: [description]
    :type info_path: [type]
    :param table_name: [description]
    :type table_name: [type]
    :param engine: [description]
    :type engine: [type]
    :param schema: [description]
    :type schema: [type]
    """
    columns_names = mapping[table_name].__table__.columns.keys()
    tableToLoad = pd.read_excel(info_path, sheet_name = table_name)
    #tableToLoad.columns = [columns_names[1:]]
    tableToLoad = tableToLoad.applymap(lambda x: preprocess(x))
    tableToLoad[columns_names[0]] = range(1,tableToLoad.shape[0]+1)
    tableToLoad = tableToLoad.reindex(columns = columns_names)
    tableToLoad.to_sql(name = table_name, schema ='bioacustica', index = False, con = engine, if_exists = 'append')


def extract_id(table_name, description):
    """Esta funcion consulta la columna que coincide con description

    :param table_name: [description]
    :type table_name: [type]
    :param description: [description]
    :type description: [type]
    :return: [description]
    :rtype: [type]
    """
    if table_name !="h_serial":
        obj = session.query(Base.classes[table_name]).filter(Base.classes[table_name].description == description).first()
    else:
        obj = session.query(Base.classes[table_name]).filter(Base.classes[table_name].h_serial == description).first()
    return obj


def extract_id_user(table_name, description):
    """Esta funcion consulta el id de los usuarios

    :param table_name: [description]
    :type table_name: [type]
    :param description: [description]
    :type description: [type]
    :return: [description]
    :rtype: [type]
    """
    obj = session.query(Base.classes[table_name]).filter(Base.classes[table_name].name == description).first()
    return obj


def load_master_tables(plantillas):
    """Esta funcion carga las tablas maestras

    :param plantillas: [description]
    :type plantillas: [type]
    """
    sheets = pd.ExcelFile(plantillas).sheet_names

    for sheet in sheets:
        try:
            load_master_table(mapping = Base.classes,
                              info_path = plantillas,
                              table_name = sheet,
                              engine = engine,
                              schema = 'bioacustica')
        except Exception as e:
            print("Error",sheet)
            print(e)


def load_tables(plantillas):
    sheets = pd.ExcelFile(plantillas).sheet_names

    for sheet in sheets:
        try:
            load_second_table(mapping = Base.classes,
                              info_path = plantillas,
                              table_name = sheet,
                              engine = engine,
                              schema = 'bioacustica')
        except Exception as e:
            print("Error",sheet)
            print(e)


def object_id(sheet_name, description):
    """
    Esta función devuelve el objeto 'sqlalchemy.ext.automap.table_name'
    para cada tabla
    """
    id = getattr(extract_id(sheet_name, description.upper()),
                                           f'id_{sheet_name}', 'No existe el atributo')
    return id


def new_plantilla(info_path):
    """
    Esta función crea una plantilla a partir de un archivo de entrada.
    Se agrega el header "description" y retorna el archivo de plantilla
    """
    file_mastertables = pd.ExcelFile(info_path)
    sheets = file_mastertables.sheet_names
    out_file = f"Plantilla{info_path}"
    writer = pd.ExcelWriter(out_file, engine='xlsxwriter')
    for sheet in sheets:
        table = file_mastertables.parse(sheet, header=None)
        table = table.rename(columns={0: "description"})

        descriptions = table["description"].values
        ids = []
        for description in descriptions:
            description = description.upper()
            id_temp = object_id(sheet, description)
            ids.append(id_temp)
        print(ids)
        table[f"id_{sheet}"] = ids
        table.to_excel(writer, sheet_name=sheet, index=False)
    writer.save()
    return out_file


def load_user(user_file):
    """Esta funcion carga los usuarios
    :param user_file: [description]
    :type user_file: [type]
    """
    try:
        load_second_table(mapping = Base.classes,
                            info_path = user_file,
                            table_name = "user",
                            engine = engine,
                            schema = 'bioacustica')
    except Exception as e:
        print("Error")
        print(e)


class CargaModelos():
    """Clase que contiene los metodos para la carga de cada tabla que no es maestra
    """
    def label(self, session, data):
        id_type = object_id("type", data["type"])

        session.add(Base.classes["label"](id_type = id_type,
                                            description = data["description"]))
        session.commit()

    def project(self, session, data):
        id_funding = object_id("funding", data["funding"])
        session.add(Base.classes["project"](id_funding = id_funding,
                                            description = data["description"]))
        session.commit()

    def sampling(self, session, data):
        id_season = object_id("season", data["season"])
        id_project = object_id("project", data["project"])
        id_cataloger = extract_id_user("user", data["cataloger"]).id_user

        session.add(Base.classes["sampling"](id_project = id_project,
                                            id_cataloger = id_cataloger,
                                            id_season = id_season,
                                            date = datetime.now(),
                                            description = data["description"]))
        session.commit()

    def h_serial(self, session, data):
        id_hardware = object_id("hardware", data["hardware"])

        session.add(Base.classes["h_serial"](id_hardware = id_hardware,
                                            h_serial = data["h_serial"]))
        session.commit()

    def catalogue(self, session, data):
        id_sampling = object_id("sampling", data["sampling"])
        id_country = object_id("country", data["country"])
        id_department = object_id("department", data["department"])
        id_municipality = object_id("municipality", data["municipality"])
        id_vereda = object_id("vereda", data["vereda"])
        id_locality = object_id("locality", data["locality"])
        id_gain = object_id("gain", data["gain"])
        id_filter = object_id("filter", data["filter"])
        id_collector = extract_id_user("user", data["collector"]).id_user
        id_h_serial = object_id("h_serial", data["h_serial"])
        id_supply = object_id("supply", data["supply"])
        id_case = object_id("case", data["case"])
        id_memory = object_id("memory", data["memory"])
        id_habitat = object_id("habitat", data["habitat"])
        id_precision = object_id("precision", data["precision"])
        id_datum = object_id("datum", data["datum"])
        id_microphone = object_id("microphone", data["microphone"])

        session.add(Base.classes["catalogue"](id_sampling = id_sampling,
                                            id_country = id_country,
                                            id_department = id_department,
                                            id_municipality = id_municipality,
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
                                            elevation = data["elevation"],
                                            height = data["height"],
                                            chunks = data["chunks"],
                                            size = data["size"],
                                            latitude = data["latitude"],
                                            longitude = data["longitude"],
                                            description = data["description"]))
        session.commit()

    def photo_path(self, session, data):
        id_catalogue = object_id("catalogue", data["catalogue"])

        session.add(Base.classes["photo_path"](id_catalogue = id_catalogue,
                                            path = data["path"]))
        session.commit()

    def catalogue_obs(self, session, data):
        id_catalogue = object_id("catalogue", data["catalogue"])

        session.add(Base.classes["catalogue_obs"](id_catalogue = id_catalogue,
                                            observation = data["observation"]))
        session.commit()

    def voucher(self, session, data):
        id_catalogue = object_id("catalogue", data["catalogue"])

        session.add(Base.classes["voucher"](id_catalogue = id_catalogue,
                                            voucher = data["voucher"]))
        session.commit()

    def record(self, session, data):
        id_catalogue = data["id_catalogue"]
        id_format =  data["id_format"]

        session.add(Base.classes["record"](id_catalogue = id_catalogue,
                                            id_format =id_format,
                                            date = data["date"],
                                            length = data["length"],
                                            size = data["size"],
                                            sample_rate = data["sample_rate"],
                                            chunk = data["chunk"],
                                            channels = data["channels"]))
        session.commit()

    def record_obs(self, session, data):
        id_record = object_id("record", data["record"])

        session.add(Base.classes["record_obs"](id_record = id_record,
                                            observation = data["observation"]))
        session.commit()

    def record_path(self, session, data):
        id_record = object_id("record", data["record"])

        session.add(Base.classes["record_path"](id_record = id_record,
                                            record_path = data["record_path"],
                                            fingerprint = data["fingerprint"]))
        session.commit()


def load_with_filter(plantillas):
    sheets = pd.ExcelFile(plantillas).sheet_names
    modelos = CargaModelos()
    for sheet in sheets:
        try:
            print(sheet)
            tableToLoad = pd.read_excel(plantillas, sheet_name = sheet)
            tableToLoad = tableToLoad.applymap(lambda x: preprocess(x))
            for index, data in tableToLoad.iterrows():
                getattr(modelos, "{}".format(sheet))(session, data)
        except Exception as e:
            print("Error",sheet)
            print(e)


def generate_records(plantillas, n_records):
    columns = Base.classes["record"].__table__.columns.keys()[1:]
    df = pd.DataFrame(columns=columns)
    catalogue = pd.read_excel(plantillas, sheet_name = "catalogue")
    formatos = pd.read_excel("MasterTablesBuenas.xlsx", sheet_name = "format")
    chunk_anterior = 0
    for index in catalogue.index:
        id_catalogue = object_id("catalogue", catalogue.loc[index, "description"].upper())
        id_format = object_id("format", "WAV".upper())
        chunks = int(catalogue.loc[index, "chunks"])
        for chunk in range(chunks):
            try:

                df.loc[chunk_anterior, "id_catalogue"] = id_catalogue
                df.loc[chunk_anterior, "id_format"] = id_format
                df.loc[chunk_anterior, "date"] = datetime.now()
                #date = datetime.now()
                df.loc[chunk_anterior, "length"] = random.randrange(2, 15, 1)
                #length = random.randrange(2, 15, 1)
                df.loc[chunk_anterior, "size"] = random.randrange(1, 1000, 1)
                #size = random.randrange(1, 1000, 1)
                df.loc[chunk_anterior, "sample_rate"] = random.randrange(9000, 22000, 1000)
                #sample_rate = random.randrange(9000, 22000, 1000)
                df.loc[chunk_anterior, "chunk"] = chunk+1
                #chunk_n = chunk+1
                df.loc[chunk_anterior, "channels"] = random.randrange(1, 2, 1)
                #channels = random.randrange(1, 2, 1)
                chunk_anterior = chunk_anterior +1
            except Exception as e:
                print("Error")
                print(e)
    writer = pd.ExcelWriter("relaciones_data_record.xlsx", engine='xlsxwriter')
    df.to_excel(writer, sheet_name="record", index=False)
    writer.save()


#load_master_tables("MasterTablesBuenas.xlsx")
#plantilla = new_plantilla("MasterTablesBuenas.xlsx")
#load_user("second_tables.xlsx")
#load_tables("relaciones_id.xlsx")

''' df =  pd.read_excel("relaciones_id.xlsx", sheet_name = "sampling")
for index, row in df.iterrows():
    sampling(session, row) '''
# id = extract_id("funding", "GHA").id_funding
# print(id)
load_master_tables("/MasterTablesBuenas.xlsx")
load_user("/second_tables.xlsx")
load_with_filter("/relaciones_data.xlsx")
#load_with_filter("relaciones_data_record.xlsx")
#generate_records("relaciones_data.xlsx", 2)


def get_headers(mapping, table_name):
    """
    Esta función obtiene los headers de una tabla.
    """
    columns_names = mapping[table_name].__table__.columns.keys()
    return columns_names


def get_tables(engine, schema):
    """
    Esta función se encarga de obtener una lista de las tablas existentes en la db.
    """
    metadata = MetaData(schema = schema)
    metadata.reflect(bind=engine)
    tables = []
    for table in metadata.tables:
        table_n = table.replace(f'{schema}.', '')
        tables.append(table_n)
    return tables


# OBTENER LISTA DE TABLAS EXISTENTES:
# existent_tables = get_tables(engine, 'bioacustica')
# print(existent_tables)

# OBTENER LISTA DE HEADERS DE CADA TABLA:
# for table in existent_tables:
#     columns = get_headers(Base.classes, table)
#     print(columns)




# #----------------------------------
#
# from mapping import Base
# from mapping import engine
# from sqlalchemy.orm import Session
#
# session = Session(engine)
#
# session.add(Base.classes["user"](name = "JUAN MANUEL",
#                                  email = "juanm.daza@udea.edu.co",
#                                  username = "juanm.daza",
#                                  roles = "ADMINISTRADOR"))
# session.commit()
#
#
# #----------------------------------
#
# from sqlalchemy.orm import Session
#
# session = Session(engine)
#
# id_funding = session.query(Base.classes["funding"]).filter(Base.classes["funding"].description == 'GHA').first().id_funding
# session.add(Base.classes["project"](id_funding = id_funding,
#                                     description = "Proyecto Piloto YNC",))
# session.commit()
#
#
# #----------------------------------
#
# import datetime
# import pandas as pd
# from mapping import Base
# from mapping import engine
# from sqlalchemy.orm import Session
#
# session = Session(engine)
#
#
# def SamplingAdd(file, session):
#
#     udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
#
#     id_season = session.query(Base.classes["season"]).filter(Base.classes["season"].description == udas.iloc[0]["season_HA"]).first().id_season
#     #id_funding = session.query(Base.classes["funding"]).filter(Base.classes["funding"].description == udas.iloc[0]["funding_PR"]).first().id_funding
#     id_project = session.query(Base.classes["project"]).filter(Base.classes["project"].description == udas.iloc[0]["project_name_PR"]).first().id_project
#     id_cataloger = session.query(Base.classes["user"]).filter(Base.classes["user"].email == udas.iloc[0]["collector_email_PR"]).first().id_user
#
#     session.add(Base.classes["sampling"](id_project = id_project,
#                                          id_cataloger = id_cataloger,
#                                          id_season = id_season,
#                                          date = datetime.datetime.now(),
#                                          description = udas.iloc[0]["id_DM"]))
#     session.commit()
#
#
#
# SamplingAdd(file = "../UDAS_20210406.xls", session = session)
#
# #----------------------------------
#
# import datetime
# import pandas as pd
# from mapping import Base
# from mapping import engine
# from sqlalchemy.orm import Session
#
# session = Session(engine)
#
#
# def CatalogueAdd(file, session, id):
#
#     udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
#
#     id_sampling = session.query(Base.classes["sampling"]).filter(Base.classes["sampling"].description == udas.iloc[id]["id_DM"]).first().id_sampling
#     id_country =  session.query(Base.classes["country"]).filter(Base.classes["country"].description == udas.iloc[id]["country"]).first().id_country
#     id_department = session.query(Base.classes["department"]).filter(Base.classes["department"].description == udas.iloc[id]["department"]).first().id_department
#     id_municipality = session.query(Base.classes["municipality"]).filter(Base.classes["municipality"].description == udas.iloc[id]["municipality"]).first().id_municipality
#     id_vereda =
#     id_gain = session.query(Base.classes["gain"]).filter(Base.classes["gain"].description == udas.iloc[id]["gain"]).first().id_gain
#     id_collector = session.query(Base.classes["user"]).filter(Base.classes["user"].description == udas.iloc[id]["collector"]).first().id_user
#     id_h_serial =
#     id_supply = session.query(Base.classes["user"]).filter(Base.classes["user"].description == udas.iloc[id]["collector"]).first().id_user
#     id_case =
#     id_memory =
#     id_habitad =
#     id_precision =
#     id_datum =
#     id_microphone =
#
#     id_project = session.query(Base.classes["project"]).filter(Base.classes["project"].description == udas.iloc[0]["project_name_PR"]).first().id_project
#     id_cataloger = session.query(Base.classes["user"]).filter(Base.classes["user"].email == udas.iloc[0]["collector_email_PR"]).first().id_user
#
#     session.add(Base.classes["catalogue"](id_sampling = id_sampling,
#                                           id_country = id_country,
#                                           id_department = id_department,
#                                           id_municipality = id_municipality,
#                                           id_vereda = id_vereda,
#                                           id_gain = id_gain,
#                                           id_collector = id_collector,
#                                           id_h_serial = id_h_serial,
#                                           id_supply = id_supply,
#                                           id_case = id_case,
#                                           id_memory = id_memory,
#                                           id_habitad = id_habitad,
#                                           id_precision = id_precision,
#                                           id_datum = id_datum,
#                                           id_microphone = id_microphone,
#                                           elevation = elevation,
#                                           height = height,
#
#
#         id_project = id_project,
#                                           id_cataloger = id_cataloger,
#                                           id_season = id_season,
#                                           date = datetime.datetime.now(),
#                                           description = udas.iloc[0]["id_DM"]))
#     session.commit()
#
#
#
# SamplingAdd(file = "../UDAS_20210406.xls", session = session)



#----------------------------------

# Temas a discutir
# 1) Dependencia entre project y funding
# 2) Coherencia entre la información de las tablas maestras y la plantilla (tocaria agregar mas información a las tablas maestras o editarlas?)
# 3) Como referenciar al usuario (por email, nombre o username)
# 4) Hablar de la plantilla (separar por hojas (sampling, catalogo y registro)) es un UDAS por sampling
# 5) Nombre del sampling (nombre del estudio) iria en description
