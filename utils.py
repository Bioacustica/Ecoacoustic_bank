from mapping import Base
from mapping import engine
from sqlalchemy.orm import Session

session = Session(engine)

session.add(Base.classes.evidence(id_evidence=1, description="Manual"))
session.add(Base.classes.evidence(id_evidence=2, description="Software"))
session.commit()

