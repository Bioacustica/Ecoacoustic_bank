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


session = Session(engine)

Globals.init()


def LoadData(file, session):

    print("Stage 1: Projects")
    AddProjects_(file, session)
    VerifyStage(session)
    
    print("Stage 2: Samplings")
    AddSamplings_(file, session)
    VerifyStage(session)
    
    print("Stage 3: Catalogues")
    AddCatalogues_(file, session)
    VerifyStage(session)
    
    print("Stage 4: Records")
    AddRecords_(file, session)
    VerifyStage(session)

    print(" ")

    session.commit()
    print("Successful transaction")
    session.close()


LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/nuevaPrueba/Ultrasonido_Dany_Urrego.xls',
        session = session) 

#LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/Tesis_Cano_20211026.xls',
#        session = session) 
#LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/UDAS_CSG_2018.xls',
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
# unificar los nombres de las tablas y del udas
# tener cuidado con llenar los campos numericos, no se puede colocar no se conoce (definir por defecto un numero)

# el project no se crea como tabla maestra, se crea con loadData ya que este depende  de id_funding
# verificar si el record fue creado ahora solo se hace a nivel de record_path
