from ast import Return
import os
import datetime
import pandas as pd
from sqlalchemy import true
from . import Globals
from .Globals import VerifyField
from .mapping import Base
from .mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)


def FailCatalogue(id_sampling, description):
    catalogue_ = session.query(Base.classes["catalogue"]).  \
        filter(Base.classes["catalogue"].id_sampling == id_sampling). \
        filter(Base.classes["catalogue"].description == description). \
        first()
    return (catalogue_ == None)


def AddCatalogue(udas, session, id, path_usb):

    try:

        Ok = True

        description_s = udas.iloc[id]["id_DM"]
        Ok = VerifyField("id_DM", description_s, id) and Ok

        project = udas.iloc[id]["project_name_PR"]
        Ok = VerifyField("project_name_PR", project, id) and Ok

        description = udas.iloc[id]["field_number_PR"]
        Ok = VerifyField("field_number_PR", description, id) and Ok

        if not Ok:
            raise

        id_project = session.query(Base.classes["project"]).  \
            filter(Base.classes["project"].description == project).  \
            first().id_project

        id_sampling = session.query(Base.classes["sampling"]).  \
            filter(Base.classes["sampling"].id_project == id_project). \
            filter(Base.classes["sampling"].description == description_s). \
            first().id_sampling

        if FailCatalogue(id_sampling, description):

            try:

                Ok = True

                country = udas.iloc[id]["country_IG"]
                Ok = VerifyField("country_IG", country, id) and Ok
                country = country.replace('"', '').upper()

                department = udas.iloc[id]["department_IG"]
                Ok = VerifyField("department_IG", department, id) and Ok
                department = department.replace('"', '').upper()

                municipality = udas.iloc[id]["municipality_IG"]
                Ok = VerifyField("municipality_IG", municipality, id) and Ok
                municipality = municipality.replace('"', '').upper()

                vereda = udas.iloc[id]["vereda_IG"]
                Ok = VerifyField("vereda_IG", vereda, id) and Ok
                vereda = vereda.replace('"', '').upper()

                locality = udas.iloc[id]["locality_IG"]
                Ok = VerifyField("locality_IG", locality, id) and Ok
                locality = locality.replace('"', '').upper()

                gain = udas.iloc[id]["gain_RE"]
                Ok = VerifyField("gain_RE", gain, id) and Ok
                gain = gain.replace('"', '').upper()

                hardware = udas.iloc[id]["recorder_RE"]
                Ok = VerifyField("recorder_RE", hardware, id) and Ok
                hardware = hardware.upper()

                print(udas.iloc[id]["rec_serial_RE"])
                h_serial = udas.iloc[id]["rec_serial_RE"]
                Ok = VerifyField("rec_serial_RE", h_serial, id) and Ok

                collector = udas.iloc[id]["collector_email_PR"]
                Ok = VerifyField("collector_email_PR", collector, id) and Ok

                elevation = udas.iloc[id]["min_elevation_IG"]
                Ok = VerifyField("min_elevation_IG", elevation, id) and Ok

                height = udas.iloc[id]["rec_height_HA"]
                Ok = VerifyField("rec_height_HA", height, id) and Ok

                latitude = udas.iloc[id]["latitude_IG"]
                Ok = VerifyField("latitude_IG", latitude, id) and Ok

                longitude = udas.iloc[id]["longitud_IG"]
                Ok = VerifyField("longitud_IG", longitude, id) and Ok

                record_dir = udas.iloc[id]["path_records_PR"]
                Ok = VerifyField("path_records_PR", record_dir, id) and Ok

                supply = udas.iloc[id]["power_source_RE"]
                Ok = VerifyField("power_source_RE", supply, id) and Ok
                supply = supply.replace('"', '').upper()

                case = udas.iloc[id]["rec_case_RE"]
                Ok = VerifyField("rec_case_RE", case, id) and Ok
                case = case.replace('"', '').upper()

                memory = udas.iloc[id]["memory_card_RE"]
                Ok = VerifyField("memory_card_RE", memory, id) and Ok
                memory = memory.replace('"', '').upper()

                filter = udas.iloc[id]["filters_RE"]
                Ok = VerifyField("filters_RE", filter, id) and Ok
                filter = filter.replace('"', '').upper()

                habitat = udas.iloc[id]["habitat_HA"]
                Ok = VerifyField("habitat_HA", habitat, id) and Ok
                habitat = habitat.replace('"', '').upper()

                precision = udas.iloc[id]["precision_IG"]
                Ok = VerifyField("precision_IG", precision, id) and Ok
                precision = precision.replace('"', '').upper()

                datum = udas.iloc[id]["datum_IG"]
                Ok = VerifyField("datum_IG", datum, id) and Ok
                datum = datum.replace('"', '').upper()

                microphone = udas.iloc[id]["microphone_RE"]
                Ok = VerifyField("microphone_RE", microphone, id) and Ok
                microphone = microphone.replace('"', '').upper()

                if not Ok:
                    raise

                try:
                    id_country = session.query(Base.classes["country"]). \
                        filter(Base.classes["country"].description == country). \
                        first().id_country

                    id_department = session.query(Base.classes["department"]). \
                        filter(Base.classes["department"].description == department). \
                        first().id_department

                    id_m = session.query(Base.classes["municipality"]). \
                        filter(Base.classes["municipality"].description == municipality). \
                        first().id_municipality

                    id_vereda = session.query(Base.classes["vereda"]). \
                        filter(Base.classes["vereda"].description == vereda). \
                        first().id_vereda

                    id_locality = session.query(Base.classes["locality"]). \
                        filter(Base.classes["locality"].description == locality). \
                        first().id_locality

                    id_gain = session.query(Base.classes["gain"]). \
                        filter(Base.classes["gain"].description == gain). \
                        first().id_gain

                    id_filter = session.query(Base.classes["filter"]). \
                        filter(Base.classes["filter"].description == filter). \
                        first().id_filter

                    id_collector = session.query(Base.classes["user"]). \
                        filter(Base.classes["user"].email == collector). \
                        first().id_user

                    id_hardware = session.query(Base.classes["hardware"]). \
                        filter(Base.classes["hardware"].description == hardware). \
                        first().id_hardware

                    # id_h_serial = session.query(Base.classes["h_serial"]). \
                    #                            filter(Base.classes["h_serial"].id_hardware == id_hardware). \
                    #                            filter(Base.classes["h_serial"].h_serial == h_serial). \
                    #                            first().id_h_serial

                    #cambiar id_harware por h_serial revisar por que se generan errores
                    id_h_serial = session.query(Base.classes["h_serial"]). \
                        filter(Base.classes["h_serial"].id_hardware == id_hardware). \
                        first().id_h_serial

                    id_supply = session.query(Base.classes["supply"]). \
                        filter(Base.classes["supply"].description == udas.iloc[id]["power_source_RE"].replace('"', '').upper()). \
                        first().id_supply

                    id_case = session.query(Base.classes["case"]). \
                        filter(Base.classes["case"].description == udas.iloc[id]["rec_case_RE"].replace('"', '').upper()). \
                        first().id_case

                    id_memory = session.query(Base.classes["memory"]). \
                        filter(Base.classes["memory"].description == udas.iloc[id]["memory_card_RE"].replace('"', '').upper()). \
                        first().id_memory

                    id_habitat = session.query(Base.classes["habitat"]). \
                        filter(Base.classes["habitat"].description == udas.iloc[id]["habitat_HA"].replace('"', '').upper()). \
                        first().id_habitat

                    id_precision = session.query(Base.classes["precision"]). \
                        filter(Base.classes["precision"].description == udas.iloc[id]["precision_IG"].replace('"', '').upper()). \
                        first().id_precision

                    id_datum = session.query(Base.classes["datum"]). \
                        filter(Base.classes["datum"].description == udas.iloc[id]["datum_IG"].replace('"', '').upper()).  \
                        first().id_datum

                    id_microphone = session.query(Base.classes["microphone"]). \
                        filter(Base.classes["microphone"].description == udas.iloc[id]["microphone_RE"].replace('"', '').upper()). \
                        first().id_microphone

                    infoDir = os.listdir(path_usb + record_dir)
                    chunks = len(infoDir)
                    size = 1
                    print("ok-------------->")
                    print(elevation)
                    print(height)
                    session.add(Base.classes["catalogue"](id_sampling=id_sampling,
                                                          id_country=id_country,
                                                          id_department=id_department,
                                                          id_municipality=id_m,
                                                          id_vereda=id_vereda,
                                                          id_locality=id_locality,
                                                          id_gain=id_gain,
                                                          id_filter=id_filter,
                                                          id_collector=id_collector,
                                                          id_h_serial=id_h_serial,
                                                          id_supply=id_supply,
                                                          id_case=id_case,
                                                          id_memory=id_memory,
                                                          id_habitat=id_habitat,
                                                          id_precision=id_precision,
                                                          id_datum=id_datum,
                                                          id_microphone=id_microphone,
                                                          elevation=elevation.tolist(),
                                                          height=height.tolist(),
                                                          chunks=chunks,
                                                          size=pd.to_numeric(
                                                              size, downcast='float'),
                                                          latitude=pd.to_numeric(
                                                              latitude, downcast='float'),
                                                          longitude=pd.to_numeric(
                                                              longitude, downcast='float'),
                                                          description=description))
                    print("  Creating " + description)

                except Exception as e:
                    print(e)
                    Globals.Bug = True

                    if not 'id_sampling' in locals():
                        print("  ERROR: id_DM - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["id_DM"]))
                    elif not 'id_country' in locals():
                        print("  ERROR: country_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["country_IG"]))
                    elif not 'id_department' in locals():
                        print("  ERROR: department_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["department_IG"]))
                    elif not 'id_m' in locals():
                        print("  ERROR: municipality_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["municipality_IG"]))
                    elif not 'id_vereda' in locals():
                        print("  ERROR: vereda_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["vereda_IG"]))
                    elif not 'id_locality' in locals():
                        print("  ERROR: locality_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["locality_IG"]))
                    elif not 'id_gain' in locals():
                        print("  ERROR: gain_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["gain_RE"]))
                    elif not 'id_filter' in locals():
                        print("  ERROR: filters_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["filters_RE"]))
                    elif not 'id_collector' in locals():
                        print("  ERROR: collector_email_PR - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["collector_email_PR"]))
                    elif not 'id_hardware' in locals():
                        print("  ERROR: recorder_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["recorder_RE"]))
                    elif not 'id_h_serial' in locals():
                        print("  ERROR: rec_serial_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["rec_serial_RE"]))
                    elif not 'id_supply' in locals():
                        print("  ERROR: power_source_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["power_source_RE"]))
                    elif not 'id_case' in locals():
                        print("  ERROR: rec_case_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["rec_case_RE"]))
                    elif not 'id_memory' in locals():
                        print("  ERROR: memory_card_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["memory_card_RE"]))
                    elif not 'id_habitat' in locals():
                        print("  ERROR: habitat_HA - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["habitat_HA"]))
                    elif not 'id_precision' in locals():
                        print("  ERROR: precision_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["precision_IG"]))
                    elif not 'id_datum' in locals():
                        print("  ERROR: datum_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["datum_IG"]))
                    elif not 'id_microphone' in locals():
                        print("  ERROR: microphone_RE - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["microphone_RE"]))
                    elif not 'elevation' in locals():
                        print("  ERROR: min_elevation_IG - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["min_elevation_IG"]))
                    elif record_dir != record_dir:
                        print("  ERROR: path_records_PR - " + str(id + 2) +
                              " ->  " + str(udas.iloc[id]["path_records_PR"]))

            except Exception as e:
                Globals.Bug = True
                print("2")
                print(e)
    except Exception as e:
        Globals.Bug = True
        print("3")
        print(e)


def AddCatalogues_(file, session, path_usb):
    
    udas = pd.read_excel(file, sheet_name="UDAS", header=0)
    
    for id in range(udas.shape[0]):

        AddCatalogue(udas, session, id, path_usb)


# verificar todos los datos antes de añadirlos a un catalogo
# estandarizar la verificacion de datos revisar (ej: FailCatalogue)


# id_catalogue = session.query(Base.classes["catalogue"]). \
#               filter(Base.classes["catalogue"].description == udas.iloc[i]["catalogue"]). \
#               first().id_catalogue

# RecordsAdd(file = udas.iloc[i]["record"],
#            id_catalogue = id_catalogue,
#            session = session)


# AddCatalogues_(file = "UDAS_20210406.xls", session = session)
