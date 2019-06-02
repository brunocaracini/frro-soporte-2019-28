# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy import create_engine
engine = create_engine('sqlite:///personas.db')
Base = declarative_base()
Base.metadata.bind = engine

class Persona(Base):
    __tablename__ = 'persona'
    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    fecha_nac = Column(DateTime, nullable=False)
    dni = Column(Integer, nullable=False)
    altura = Column(Integer, nullable=False)

def crear_tabla():
    Base.metadata.create_all(engine)

def borrar_tabla():
    Persona.__table__.drop(engine)

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper





