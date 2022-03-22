
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

session.add(Base.classes["user"](name = "JUAN MANUEL",
                                 email = "juanm.daza@udea.edu.co",
                                 username = "juanm.daza",
                                 roles = "ADMINISTRADOR"))
session.commit()

