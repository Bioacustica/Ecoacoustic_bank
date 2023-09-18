import pandas as pd
from . import Globals
from .Globals import VerifyStage
from .mapping import Base
from .mapping import engine
from sqlalchemy.orm import Session

from .AddProject import AddProjects_
from .AddSampling import AddSamplings_
from .AddCatalogue import AddCatalogues_
from .AddRecord import AddRecords_
import subprocess
import sys



session = Session(engine)

Globals.init()

def LoadData(file, usbSelected):
    Globals.init()
    path_static = "/code/usb/"
    path_usb = ""
    content_usbs = subprocess.check_output(['ls', path_static])
    resultado_decodificado = content_usbs.decode('utf-8')
    print("resultado_decodificado", resultado_decodificado)
    num_usbs_connected = len(resultado_decodificado.split("\n")) -1 
    print("num_usbs_connected", num_usbs_connected)

    print(Globals.Bug)

    if (usbSelected != ""):
        path_usb = path_static +  usbSelected + "/"  
    elif(num_usbs_connected > 1):
        return resultado_decodificado.split("\n")
    elif(num_usbs_connected == 0):
        print("Por favor revisar que se tenga conectada una sola USB")
        Globals.Bug = True
    else:
        path_usb = path_static +  resultado_decodificado.strip() + "/"
    
    print(path_usb)

    VerifyStage(session)
    

    print("Stage 1: Projects")
    AddProjects_(file, session)
    VerifyStage(session)

    print("Stage 2: Samplings")
    AddSamplings_(file, session)
    VerifyStage(session)

    print("Stage 3: Catalogues")
    AddCatalogues_(file, session, path_usb)
    VerifyStage(session)

    print("Stage 4: Records")
    AddRecords_(file, session, path_usb)
    VerifyStage(session)

    print(" ")

    session.commit()
    print("Successful transaction")




# LoadData(file = './Test_ETL/Ultrasonido_Dany_Urrego.xls',
#        session = session)

# LoadData(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/Tesis_Cano_20211026.xls',
#        session = session)
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
# como hacer la consulta para obtener el id_record tiene que crearse primero en la base de datos
# unificar los nombres de las tablas y del udas
# tener cuidado con llenar los campos numericos, no se puede colocar no se conoce (definir por defecto un numero)

# el project no se crea como tabla maestra, se crea con loadData ya que este depende  de id_funding
# verificar si el record fue creado ahora solo se hace a nivel de record_path
# Se estan generando varios proyect_ID en NO SE CONOCE

# Antes de cargar datos se debe:
# - Cargar las tablas maestras
# - Generar los usuarios
#   (si sale este  ERROR: collector_email_PR - 2 ->  dany.urrego@udea.edu.co
#    posiblemente es por que no se a generado el usuario)
# - Generar las grabadoras