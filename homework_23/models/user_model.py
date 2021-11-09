from sqlalchemy import Integer, Column, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
    age = Column(Integer)
