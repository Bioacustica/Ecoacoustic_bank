import pandas as pd
import Globals
from Globals import VerifyStage
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
<<<<<<< HEAD

    print("Stage 2: Samplings")
    AddSamplings_(file, session)

    print("Stage 3: Catalogues")
    AddCatalogues_(file, session)

=======
    VerifyStage(session)
    
    print("Stage 2: Samplings")
    AddSamplings_(file, session)
    VerifyStage(session)
    
    print("Stage 3: Catalogues")
    AddCatalogues_(file, session)
    VerifyStage(session)
    
>>>>>>> cda1a6a1114c67153389ea076204e801f7f5161c
    print("Stage 4: Records")
    AddRecords_(file, session)
    VerifyStage(session)

    print(" ")

<<<<<<< HEAD
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
=======
    session.commit()
    print("Successful transaction")
    session.close()


LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/nuevaPrueba/Ultrasonido_Dany_Urrego.xls',
        session = session) 

#LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/Tesis_Cano_20211026.xls',
#        session = session) 
#LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/UDAS_CSG_2018.xls',
#         session = session) 
>>>>>>> cda1a6a1114c67153389ea076204e801f7f5161c


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
<<<<<<< HEAD
=======
# unificar los nombres de las tablas y del udas
# tener cuidado con llenar los campos numericos, no se puede colocar no se conoce (definir por defecto un numero)

# el project no se crea como tabla maestra, se crea con loadData ya que este depende  de id_funding
# verificar si el record fue creado ahora solo se hace a nivel de record_path
>>>>>>> cda1a6a1114c67153389ea076204e801f7f5161c
