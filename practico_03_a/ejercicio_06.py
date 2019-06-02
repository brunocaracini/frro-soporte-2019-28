# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import datetime
from ejercicio_01 import Persona
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from ejercicio_01 import borrar_tabla, crear_tabla
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('sqlite:///personas.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

class PersonaPeso(Base):
    __tablename__ = 'pesos'
    id_peso = Column(Integer, primary_key=True,autoincrement=True)
    fecha = Column(DateTime, nullable=False)
    peso = Column(Integer, nullable=False)
    id_persona = Column(Integer, ForeignKey('persona.id_persona'))
    persona = relationship(Persona)

def crear_tabla_peso():
    Base.metadata.create_all(engine)

def borrar_tabla_peso():
    PersonaPeso.__table__.drop(engine)

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper