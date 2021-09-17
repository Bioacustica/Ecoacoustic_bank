from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('postgresql://animalesitm:animalesitm@172.19.0.2:5432/animalesitm')

m = MetaData(schema = 'bioacustica')
Base = automap_base(bind=engine, metadata=m)

Base.prepare(engine = engine, reflect=True)

Evidence = Base.classes.evidence

Base.classes["evidence"]