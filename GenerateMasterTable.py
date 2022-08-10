import pandas as pd
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def GenerateMasterTable(file, session):
    # file: 'masterTable.xlsx'
    sheetToGenerate = [
        "format",
        "country",
        "department",
        "municipality",
        "vereda",
        "locality",
        "hardware",
        "case",
        "microphone",
        "memory",
        "supply",
        "datum",
        "precision",
        "habitat",
        "season",
        "gain",
        "project",
        "funding",
    ]

    writer = pd.ExcelWriter(file, engine="xlsxwriter")

    for sheet in sheetToGenerate:
        try:
            infoSheet = pd.DataFrame(
                session.query(Base.classes[sheet].description).all()
            )
            infoSheet.to_excel(writer, sheet_name=sheet, index=False, header=False)
        except:
            print("Error: Generating " + sheet)
            infoSheet = pd.DataFrame()
            infoSheet.to_excel(writer, sheet_name=sheet, index=False, header=False)

    writer.save()


# GenerateMasterTable(file = '/home/andres/Proyectos/Software/Bioacustico/bioacustica/MasterTablesGenerada.xlsx',
#                    session = session)
