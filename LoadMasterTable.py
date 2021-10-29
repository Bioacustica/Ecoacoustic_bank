import pandas as pd
import xlsxwriter
from sqlalchemy.orm import Session, load_only

from mapping import Base
from mapping import engine

session = Session(engine)


def load_master_table(mapping, info_path, table_name, engine, schema):
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
    tableToLoad.to_sql(name = table_name, schema ='bioacustica', index = False, con = engine, if_exists = 'append')


def extract_id(table_name, description):
    obj = session.query(Base.classes[table_name]).filter(Base.classes[table_name].description == description).first()
    return obj


def load_master_tables(plantillas):
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


def object_id(sheet_name: str, description: str) -> object:
    """
    Esta función devuelve el objeto 'sqlalchemy.ext.automap.table_name'
    para cada tabla
    """
    if sheet_name == "country":
        return extract_id("country", description).id_country
    elif sheet_name == "department":
        return extract_id("department", description).id_department
    elif sheet_name == "municipality":
        return extract_id("municipality", description).id_municipality
    elif sheet_name == "vereda":
        return extract_id("vereda", description).id_vereda
    elif sheet_name == "locality":
        return extract_id("locality", description).id_locality
    elif sheet_name == "hardware":
        return extract_id("hardware", description).id_hardware
    elif sheet_name == "case":
        return extract_id("case", description).id_case
    elif sheet_name == "microphone":
        return extract_id("microphone", description).id_microphone
    elif sheet_name == "memory":
        return extract_id("memory", description).id_memory
    elif sheet_name == "supply":
        return extract_id("supply", description).id_supply
    elif sheet_name == "format":
        return extract_id("format", description).id_format
    elif sheet_name == "datum":
        return extract_id("datum", description).id_datum
    elif sheet_name == "precision":
        return extract_id("precision", description).id_precision
    elif sheet_name == "habitat":
        return extract_id("habitat", description).id_habitat
    elif sheet_name == "season":
        return extract_id("season", description).id_season
    elif sheet_name == "filter":
        return extract_id("filter", description).id_filter
    elif sheet_name == "gain":
        return extract_id("gain", description).id_gain
    elif sheet_name == "funding":
        return extract_id("funding", description).id_funding
    elif sheet_name == "type":
        return extract_id("type", description).id_type


def new_plantilla(info_path: str) -> str:
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
        table[f"id_{sheet}"] = ids
        table.to_excel(writer, sheet_name=sheet, index=False)
    writer.save()
    return out_file


# load_master_tables("MasterTablesBuenas.xlsx")
plantilla = new_plantilla("MasterTablesBuenas.xlsx")


# id = extract_id("funding", "GHA").id_funding
# print(id)


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
