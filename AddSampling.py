import datetime
import pandas as pd
import Globals
from Globals import VerifyField
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

def FailSampling(id_project, description):
    sampling_ = session.query(Base.classes["sampling"]).  \
                               filter(Base.classes["sampling"].id_project == id_project). \
                               filter(Base.classes["sampling"].description == description). \
                               first()
    return(sampling_ == None)

def AddSampling(udas, session, id):

    try:

        Ok = True

        description = udas.iloc[id]["id_DM"]
        Ok = VerifyField("id_DM", description, id) and Ok 
        
        project = udas.iloc[id]["project_name_PR"]
        Ok = VerifyField("project_name_PR", project, id) and Ok

        if not Ok:
            raise

        id_project = session.query(Base.classes["project"]).  \
                                filter(Base.classes["project"].description == project).  \
                                first().id_project

        if FailSampling(id_project, description):
            try:
                
                Ok = True
                
                season = udas.iloc[id]["season_HA"]
                Ok = VerifyField("season_HA", project, id) and Ok

                cataloger = udas.iloc[id]["collector_email_PR"]
                Ok = VerifyField("collector_email_PR", cataloger, id) and Ok
                
                if not Ok:
                    raise

                id_season = session.query(Base.classes["season"]).  \
                                        filter(Base.classes["season"].description == season).  \
                                        first().id_season
                
                id_cataloger = session.query(Base.classes["user"]).  \
                                            filter(Base.classes["user"].email == cataloger).  \
                                            first().id_user
                
                session.add(Base.classes["sampling"](id_project = id_project,
                                                     id_cataloger = id_cataloger,
                                                     id_season = id_season,
                                                     date = datetime.datetime.now(),
                                                     description = description))
                
                print("  Creating " + udas.iloc[id]["id_DM"])
                
            except:
                Globals.Bug = True
                if not 'id_season' in locals():
                    print("ERROR: season_HA - " + str(id + 2) + " ->  " + str(udas.iloc[id]["season_HA"]) )
                elif not 'id_project' in locals():
                    print("ERROR: project_name_PR - " + str(id + 2) + " ->  " + str(udas.iloc[id]["project_name_PR"]) )
                elif not 'id_cataloger' in locals():
                    print("ERROR: collector_email_PR - " + str(id + 2) + " ->  " + str(udas.iloc[id]["collector_email_PR"]) )   
    except:
        Globals.Bug = True 



def AddSamplings_(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for id in range(udas.shape[0]):
        
        AddSampling(udas, session, id)


#AddSamplings_(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/UDAS_20210406.xls',
#             session = session)




