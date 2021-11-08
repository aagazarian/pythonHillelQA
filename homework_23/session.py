from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("postgresql://arpine:Password123@localhost/store")

__session = sessionmaker(engine)
session: Session = __session()
