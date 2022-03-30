import datetime
import pandas as pd
from mapping import Bug
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def AddSampling(udas, session, id):
    
    try:
        id_season = session.query(Base.classes["season"]).filter(Base.classes["season"].description == udas.iloc[id]["season_HA"]).first().id_season
        id_project = session.query(Base.classes["project"]).filter(Base.classes["project"].description == udas.iloc[id]["project_name_PR"]).first().id_project
        id_cataloger = session.query(Base.classes["user"]).filter(Base.classes["user"].email == udas.iloc[id]["collector_email_PR"]).first().id_user
        
        session.add(Base.classes["sampling"](id_project = id_project,
                                             id_cataloger = id_cataloger,
                                             id_season = id_season,
                                             date = datetime.datetime.now(),
                                             description = udas.iloc[id]["id_DM"]))
        session.commit()
    except:
        Bug = True
        if not 'id_season' in locals():
            print("ERROR: season_HA - " + str(id + 2) + " ->  " + str(udas.iloc[id]["season_HA"]) )
        elif not 'id_project' in locals():
            print("ERROR: project_name_PR - " + str(id + 2) + " ->  " + str(udas.iloc[id]["project_name_PR"]) )
        elif not 'id_cataloger' in locals():
            print("ERROR: collector_email_PR - " + str(id + 2) + " ->  " + str(udas.iloc[id]["collector_email_PR"]) )    



def AddSamplings_(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for id in range(udas.shape[0]):
        
        AddSampling(udas, session, id)


#AddSamplings_(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/UDAS_20210406.xls',
#             session = session)




