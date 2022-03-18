import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

def AddProject(udas, session, id):
    
    try:
        id_funding = session.query(Base.classes["funding"]).filter(Base.classes["funding"].description == udas.iloc[id]["funding_PR"]).first().id_funding
        session.add(Base.classes["project"](id_funding = id_funding,
                                            description = udas.iloc[id]["project_name_PR"]))
    except:
        print("id_funding - " + str(id+1) + " ->  " + str(udas.iloc[id]["funding_PR"]) )



def AddProjects(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    
    for id in range(udas.shape[0]):
        
        AddProject(udas, session, id)



AddProjects(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/UDAS_20210406.xls', session = session)


