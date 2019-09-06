# Implementar los metodos de la capa de negocio de socios.

from ejercicio_01TP5 import Socio
from ejercicio_02TP5 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        return self.datos.todos()

    def alta(self, socio):
        if (self.regla_1(socio) and self.regla_2(socio) and self.regla_3()):
            self.datos.alta(socio)
            return socio
        else:
            return None

    def baja(self, id_socio):
        return self.datos.baja(id_socio)

    def modificacion(self, socio_mod, id_socio):
        if (self.regla_2(socio_mod) == True):
            return self.datos.modificacion(socio_mod, id_socio)
        else:
            return None
            
    def regla_1(self, socio):
        socio_repetido = self.buscar_dni(socio.dni)
        if socio_repetido == False:
            return True
        else:
            #Excepcion de dni existente
            raise DniRepetido('El dni ya se encuentra registrado')

    def regla_2(self, socio):
        if (len(socio.nombre) < self.MIN_CARACTERES or len(socio.nombre)> 15):
            #Excepcion de min caracteres nombre
            raise LongitudInvalida('Error en la longitud del nombre, debe tener entre 3 y 15 caracteres.')
        elif (len(socio.apellido) < self.MIN_CARACTERES or len(socio.apellido)> 15):
            #Excepcion de min caracteres apellido
            raise LongitudInvalida('Error en la longitud del apellido, debe tener entre 3 y 15 caracteres.')
        else:
            return True

    def regla_3(self):
        if len(self.datos.todos()) > self.MAX_SOCIOS:
            #Excepción de maximo socios
            raise MaximoAlcanzado('Error: Se ha alcanzado el maximo de socios')
        else:
            return True
