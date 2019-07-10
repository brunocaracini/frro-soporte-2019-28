# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy import create_engine

engine = create_engine('sqlite:///socios.db')
Base = declarative_base()
Base.metadata.bind = engine


class Socio(Base):
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key = True, autoincrement=True)
    dni = Column(Integer)
    nombre = Column(Integer)
    apellido = Column(Integer)
    
def crear_tabla():
    Base.metadata.create_all(engine)

crear_tabla()