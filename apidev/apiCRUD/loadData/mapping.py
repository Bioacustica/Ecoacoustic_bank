from socket import timeout
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData


engine = create_engine('postgresql://animalesitm:animalesitm@postgres/animalesitm',
                       connect_args={'connect_timeout': 100})

m = MetaData(schema='bioacustica')
Base = automap_base(bind=engine, metadata=m)

Base.prepare(engine=engine, reflect=True)
