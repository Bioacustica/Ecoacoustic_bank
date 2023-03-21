
from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

# session.add(Base.classes["user"](name = "JUAN MANUEL",
#                                  email = "juanm.daza@udea.edu.co",
#                                  username = "juanm.daza",
#                                  roles = "ADMINISTRADOR"))

#session.add(Base.classes["user"](name = "ESTEFANY CANO",
#                                 email = "canoestefany@gmail.com",
#                                 username = "estefany.cano",
#                                 roles = "ADMINISTRADOR"))

session.add(Base.classes["user"](name = "Dany Urrego",
                                 email = "dany.urrego@udea.edu.co",
                                 username = "Dany.Urrego",
                                 roles = "ADMINISTRADOR"))
                                

session.commit()

