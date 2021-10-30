from mapping import engine
from mapping import Base
from sqlalchemy.orm import Session

session = Session(engine)

pais = Base.classes.country
#answer = session.query(pais).filter(pais.id_country==1).first()
#answer.description

answer = session.query(pais).filter(pais.description == 'COLOMBIA').first()
answer.id_country


from mapping import engine
from mapping import Base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

pais = Base.classes.country
session.query(pais).filter(pais.id_country==1).first()

