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
    tableToLoad = pd.read_excel(info_path, sheet_name = table_name, header = None, engine = 'openpyxl')
    tableToLoad = tableToLoad.applymap(lambda x: x.replace('"','').upper())
    tableToLoad.columns = [columns_names[1]]
    tableToLoad[columns_names[0]] = range(1,tableToLoad.shape[0]+1)
    tableToLoad = tableToLoad.reindex(columns = columns_names)
    
    for i in range(len(tableToLoad)):
        try:
            tableToLoad.iloc[i:i+1].to_sql(name = table_name, con = engine, schema = 'bioacustica', if_exists = 'append', index = False)
        except:
            pass


def LoadMasterTables(info_path, mapping, engine):
    
    sheets = pd.ExcelFile(info_path, engine = 'openpyxl').sheet_names
    
    for sheet in sheets:
        try:
            LoadMasterTable(mapping = mapping,
                            info_path = info_path,
                            table_name = sheet,
                            engine = engine,
                            schema = 'bioacustica')
        except:
            print("Error",sheet)


LoadMasterTables(info_path = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/MasterTablesGenerada.xlsx',
                 mapping = Base.classes,
                 engine = engine)

