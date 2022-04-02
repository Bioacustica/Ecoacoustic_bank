import pandas as pd
import Globals
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

def AddProject(udas, session, id):
    
    try:
        funding = str(udas.iloc[id]["funding_PR"]).upper()
        id_funding = session.query(Base.classes["funding"]). \
                                   filter(Base.classes["funding"].description == funding).  \
                                   first().id_funding
        id_project = session.query(Base.classes["project"]).  \
                                   filter(Base.classes["project"].id_funding == id_funding).  \
                                   filter(Base.classes["project"].description == udas.iloc[id]["project_name_PR"] ). \
                                   first().id_project
        if id_project != id_project:
            session.add(Base.classes["project"](id_funding = id_funding,
                                                description = udas.iloc[id]["project_name_PR"]))
            print("  Creating " + udas.iloc[id]["project_name_PR"])
    except:
        Globals.Bug = True
        print("ERROR: funding_PR - " + str(id + 2) + " ->  " + str(funding) )



def AddProjects_(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for id in range(udas.shape[0]):
        
        AddProject(udas, session, id)



#AddProjects(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/UDAS_20210406.xls',
#            session = session)




