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
    tableToLoad.to_sql(name = table_name, schema ='bioacustica', index = False, con = engine, if_exists = 'append')



sheets = pd.ExcelFile('MasterTables.xls').sheet_names

for sheet in sheets:
    try:
        LoadMasterTable(mapping = Base.classes,
                        info_path = 'MasterTables.xls',
                        table_name = sheet,
                        engine = engine,
                        schema = 'bioacustica')
    except:
        print("Error",sheet)

