from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.exc import OperationalError

engine = create_engine('postgresql://animalesitm:animalesitm@postgres:5432/animalesitm')

db_status = False

while not db_status:
    try:
        engine.connect()
        db_status = True
    except OperationalError:
        print("NO EXISTE DB ")

m = MetaData(schema = 'bioacustica')
Base = automap_base(bind=engine, metadata=m)

Base.prepare(engine = engine, reflect=True)
