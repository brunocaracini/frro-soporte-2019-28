# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import mysql.connector

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    if buscar_persona(id_persona):
        connection = mysql.connector.connect(user="Bruno", password="12345", host="localhost", database = "brunobd")
        cursor = connection.cursor()
        cSQL = "SELECT FECHA FROM persona_peso WHERE IdPersona = %s"
        cursor.execute(cSQL, (id_persona, ))
        results = cursor.fetchall()
        if len(results) > 0:
            max_date = results[0][0]
            for date_array in results:
                if date_array[0] > max_date:
                    max_date = date_array[0]
            if fecha < max_date:
                return False
                
        cSQL = "INSERT INTO persona_peso (IdPersona, Peso, Fecha) VALUES (%s, %s, %s)"
        cursor.execute(cSQL, (id_persona, peso, fecha))
        connection.commit()
        return id_persona

    else: 
        return False

    
        


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
