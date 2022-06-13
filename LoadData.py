import pandas as pd
import Globals
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

from AddProject import AddProjects_
from AddSampling import AddSamplings_
from AddCatalogue import AddCatalogues_
from AddRecord import AddRecords_

from GenerateMasterTable import GenerateMasterTable

session = Session(engine)

Globals.init()


def LoadData(file, session):

    print("Stage 1: Projects")
    AddProjects_(file, session)

    print("Stage 2: Samplings")
    AddSamplings_(file, session)

    print("Stage 3: Catalogues")
    AddCatalogues_(file, session)

    print("Stage 4: Records")
    AddRecords_(file, session)

    print(" ")

    if Globals.Bug:
        session.rollback()
        print("Reversing transaction")
        print("Generating: Master Table file")
        GenerateMasterTable(file="MasterTablesGenerada_.xlsx", session=session)
    else:
        session.commit()
        print("Successful transaction")

    Globals.Bug = False
    session.close()


LoadData(file="./Tesis_Cano_20211026.xls", session=session)
# LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/UDAS_CSG_2018.xls',
#         session = session)


# incrementar el ID que se imprime (ok)
# cuando se genere los erroes descargar el ultimo masterTable (ok)
# quitar tildes
# precision_IG - 1 y 2 revisar por que sale error en las primeras filas (ok)
# Agregar al generateMasterTable filter, no se agrego por que en la tabla esta mal escrita el campo
# description aparece como decription (ok)
# revisar si es el master table generado se puede sobreescibir (si)


# TO-DO
# Se debe generar id_h_serial (en esta oportunidad se genero manual desde el pgadmin)
# como hacer la consulta para obtener el id_record tiene que crearse primero en la base de datos
