# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import mysql.connector
import datetime

from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    connection = mysql.connector.connect(user="Bruno", password="12345", host="localhost", database = "brunobd")
    cursor = connection.cursor()
    #"CREATE TABLE IF NOT EXISTS persona_peso (  `IdPersona` INT NOT NULL, Peso INT NULL, Fecha DATETIME, PRIMARY KEY (`IdPersona`,`Fecha`), CONSTRAINT `IdPersona` FOREIGN KEY (`IdPersona`) REFERENCES `brunobd`.`persona` (`IdPersona`))")
    cursor.execute("CREATE TABLE `brunobd`.`persona_peso` (`IdPersona` INT NOT NULL,`Peso` INT NULL,`Fecha` DATETIME NOT NULL,PRIMARY KEY (`IdPersona`, `Fecha`),CONSTRAINT `IdPersona`FOREIGN KEY (`IdPersona`)REFERENCES `brunobd`.`persona` (`IdPersona`))")


def borrar_tabla_peso():
    connection = mysql.connector.connect(user="Bruno", password="12345", host="localhost", database = "brunobd")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS persona_peso")


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
