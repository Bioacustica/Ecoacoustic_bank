import pandas as pd
from . import Globals
from .Globals import VerifyField
from .mapping import Base
from .mapping import engine
from sqlalchemy.orm import Session
import sys

session = Session(engine)


def FailProject(id_funding, description):
    project_ = session.query(Base.classes["project"]).  \
        filter(Base.classes["project"].id_funding == id_funding).  \
        filter(Base.classes["project"].description == description). \
        first()
    return (project_ == None)


def AddProject(udas, session, id):
    #print("udas", udas)
    #print("session", session)
    #print("id", id)
    try:

        Ok = True

        funding = udas.iloc[id]["funding_PR"]
        Ok = VerifyField("funding_PR", funding, id) and Ok
        funding = str(funding).upper()

        project = udas.iloc[id]["project_name_PR"]
        Ok = VerifyField("project_name_PR", project, id) and Ok

        if not Ok:
            raise Exception
        id_funding = session.query(Base.classes["funding"]). \
            filter(Base.classes["funding"].description == funding).  \
            first().id_funding

        if FailProject(id_funding, project):

            try:

                id_project = (
                    session.query(Base.classes["project"])
                    .filter(Base.classes["project"].description == project)
                    .first()
                )
                
                #print(id_project)

                if id_project == None:
                    session.add(Base.classes["project"](id_funding = id_funding,
                                                        description = project))
                    print("  Creating " + project)

            except Exception as e:

                print(e)

                Globals.Bug = True

                if not 'id_funding' in locals():
                    print("  ERROR: funding_PR - " +
                          str(id + 2) + " ->  " + str(funding))

    except Exception as e:

        Globals.Bug = True
        raise Exception

        if not 'id_funding' in locals():
            print("  ERROR: funding_PR - " +
                  str(id + 2) + " ->  " + str(funding))


def AddProjects_(file, session):
    
    udas = pd.read_excel(file, sheet_name = "UDAS", header = 0)
    # se podria pensar en poner un try catch por si hay problemas con la lectura del excel 
    # o esta mal especificado el sheet_name 
    for id in range(udas.shape[0]):

        AddProject(udas, session, id)


# AddProjects(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/UDAS_20210406.xls',
#            session = session)
