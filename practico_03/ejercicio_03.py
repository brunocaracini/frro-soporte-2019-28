# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import mysql.connector

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    connection = mysql.connector.connect(user="Bruno", password="12345", host="localhost", database = "brunobd")
    cursor = connection.cursor()
    cSQL = "SELECT IdPersona FROM PERSONA WHERE IdPersona = %s"
    cursor.execute(cSQL, (id_persona, ))
    result = cursor.fetchall()
    if len(result) > 0:
        cSQL = "DELETE FROM persona WHERE IdPersona = %s"
        cursor.execute(cSQL, (id_persona, ))
        connection.commit()
        return True
    else:
        print("No existe esa persona")
        return False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
