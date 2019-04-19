#!/usr/bin/env python3

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Busca(Base):
    __tablename__ = 'busca'

    id = Column(Integer, primary_key=True)
    chat = Column(Integer)
    positions = Column(Integer)
    number = Column(Integer)
    typeSearch = Column(String)
    tempoExecucao = Column(Float)

    def __repr__(self):
        return "<Busca(id={}, chat={}, positions={},number={},typeSearch='{}',tempoExecucao={})>".format(
            self.id, self.chat, self.positions,self.number,self.typeSearch,self.tempoExecucao
        )

Base.metadata.create_all(engine)

if __name__ == '__main__':
    pass
