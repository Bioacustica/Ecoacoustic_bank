import pandas as pd
from .mapping import Base
from .mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def LoadHSerial():
    hardwares = session.query(Base.classes["hardware"]).all()
    for hardware in hardwares:
        session.add(Base.classes["h_serial"](id_hardware=hardware.id_hardware,
                                             h_serial="NO SE CONOCE"))
    session.commit()

def RemoverDuplicados(dataframe, descriptions):
    description_list = [desc[0] for desc in descriptions]
    dataframe_filtrado = dataframe[~dataframe['description'].isin(description_list)]
    return dataframe_filtrado


def LoadMasterTable(mapping, info_path, table_name, engine, schema):
    # mapping: sqlalchemy.ext.automap (Base.classes)
    # info_path: string with file path ('MasterTables.xls')
    # table_name: string with table name ('evidence')
    # engine: database conection
    # schema: ('bioacustica')
    def withoutAccent(s):
        # Replace accent marks
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    # ----------
    columns_names = mapping[table_name].__table__.columns.keys()

    elements = session.query(Base.classes[table_name]).all()
    #print("44",len(elements))
    if len(elements) == 0:
        id_end = 0
    else:
        end_element = elements[-1]
        id_end = getattr(end_element, columns_names[0])

    tableToLoad = pd.read_excel(
        info_path, sheet_name = table_name, header = None, engine = 'openpyxl')
    #print("44",tableToLoad)
    tableToLoad = tableToLoad.applymap(lambda x: withoutAccent(x))
    tableToLoad = tableToLoad.applymap(lambda x: x.replace('"', '').upper())
    tableToLoad.columns = [columns_names[1]]
    #print("50",tableToLoad)

    #print("52",id_end)
    descriptions = session.query(Base.classes[table_name].description).all()
    #print(tableToLoad)
    #print(descriptions)
    #print("55",descriptions)

    tableToLoad = RemoverDuplicados(tableToLoad, descriptions)
    tableToLoad[columns_names[0]] = range(id_end + 1, id_end + tableToLoad.shape[0] + 1)
    tableToLoad = tableToLoad.reindex(columns = columns_names)
    #print("69",tableToLoad)

    try:
        if(len(tableToLoad) > 0):
            tableToLoad.to_sql(name = table_name, con = engine,
                               schema = 'bioacustica', if_exists = 'append', index = False)
            print("Updating",table_name,"...")
            print(tableToLoad)
            print(" |-> Table",table_name,"was updated.")
        else:
            print(" |-> Table",table_name,"is updated.")
    except Exception as e:
        print("ERROR in",table_name)
        print(tableToLoad)
        print(e)


def LoadMasterTables(info_path):
    print("---------------------------------")
    print("Loading", info_path, "...")
    print("---------------------------------")
    sheets = pd.ExcelFile(info_path, engine = 'openpyxl').sheet_names
    #sheets.remove('project') # saldria error si project no esta en la lista
    #sheets = ["gain","country"]

    # print("sheets", sheets)
    for sheet in sheets:
        try:
            LoadMasterTable(mapping = Base.classes,
                            info_path = info_path,
                            table_name = sheet,
                            engine = engine,
                            schema = 'bioacustica')

        except Exception as e:
            print(sheet," ",e)

    # LoadHSerial()

    # LoadMasterTables(info_path='./Test_ETL/MasterTables_v1.xlsx',
    #                  mapping=Base.classes,
    #                  engine=engine)
