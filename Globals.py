from ast import Global
import sys
from GenerateMasterTable import GenerateMasterTable


def init():
    global Bug
    Bug = False


def VerifyField(field, value, id):
    if value != value:
        print("  ERROR: " + field + " - " + str(id + 2) + " ->  " + str(value))
        return False
    else:
        return True

def VerifyStage(session):
    if Bug == True:
        session.rollback()
        print("Reversing transaction")
        print("Generating: Master Table file")
        GenerateMasterTable(file = "MasterTablesGenerada_v1.xlsx",
                            session = session)
        session.close()
        sys.exit()
