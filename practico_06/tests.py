# Implementar los casos de prueba descriptos.

import unittest

from ejercicio_01TP5 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
         # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

        # dni repetido
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombremayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juuuuuuuuuuuuuuuuuuuaaaaaaaaannn', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Peeeeeerrrrrreeeeeezzzzzzzzzzz')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.regla_3())

        # Se añaden mas de 200 socios
        for y in range(0, 200):
            invalido = Socio(nombre='Juan', apellido='Perez')
            self.ns.alta(invalido)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3())

    def test_baja(self):
        # valida baja
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.baja(valido.id_socio))

        # Se borra un socio que no se ha cargado
        invalido = Socio(dni = 12345789, nombre='Juan', apellido='Perez')
        self.ns.baja(invalido)
        self.assertFalse(self.ns.baja(invalido.id_socio))

    def test_buscar(self):
        # valida busqueda
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.buscar(valido.id_socio))

        # Se busca un socio que no se ha cargado
        invalido = Socio(dni = 41028971, nombre='Bruno', apellido='Caracini')
        self.assertFalse(self.ns.buscar(invalido.id_socio))


    def test_buscar_dni(self):
        # valida busqueda por dni
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.buscar_dni(valido.dni))

        # Se busca por dni un socio que no se ha cargado
        invalido = Socio(dni = 41028971, nombre='Bruno', apellido='Caracini')
        self.assertFalse(self.ns.buscar_dni(invalido.dni))

    def test_todos(self):
        # valida devoucion de un arreglo de socios no vacio, cargando uno para asegurar la no nulidad de socios
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        assert self.ns.todos() != None 

    def test_modificacion(self):
         # valida modificacion de socio existente
        valido = valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        valido_mod = Socio(dni=12345679, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.modificacion(valido_mod))

        # Se modifica socio inexistente
        invalido = Socio(dni = 41028971, nombre='Bruno Tomas', apellido='Caracini')
        self.assertFalse(self.ns.modificacion(invalido))
