import pandas as pd
from mapping import Bug
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

from AddProject import AddProjects_
from AddSampling import AddSamplings_
from AddCatalogue import AddCatalogues_
from AddRecord import AddRecords_

from GenerateMasterTable import GenerateMasterTable

session = Session(engine)


def LoadData(file, session):
    
    print("Stage 1: Projects")
    AddProjects_(file, session)
    
    print("Stage 2: Samplings")
    AddSamplings_(file, session)
    
    print("Stage 3: Catalogues")
    AddCatalogues_(file, session)
    
    print("Stage 4: Records")
    AddRecords_(file, session)

    if Bug:
        print("Generating: Master Table file")
        GenerateMasterTable(file = "MasterTablesGenerada.xls",
                            session = session)
    Bug = False


LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/UDAS_20210406.xls',
         session = session) 

# incrementar el ID que se imprime
# cuando se genere los erroes descargar el ultimo masterTable (ok)
# quitar tildes
# precision_IG - 1 y 2 revisar por que sale error en las primeras filas (ok)