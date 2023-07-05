import unittest
from datetime import datetime
from dados import *

class TestReservaDiaria(unittest.TestCase):
    def runTest(self):
        reserva = Reserva(
            quartos=[Quarto(valor=100.0), Quarto(valor=50.0)]
        )
        self.assertEqual(reserva.diaria(), 150.0, "Valor da diaria incorreto.")

class TestReservaSubtotal(unittest.TestCase):
    def runTest(self):
        reserva = Reserva(
            check_in=datetime.strptime("2023-07-07", "%Y-%m-%d"),
            check_out=datetime.strptime("2023-07-10", "%Y-%m-%d"), 
            quartos=[Quarto(valor=100.0), Quarto(valor=50.0)]
        )
        self.assertEqual(reserva.subtotal(), 450.0, "Subtotal incorreto.")

class TestReservaCalcConsumo(unittest.TestCase):
    def runTest(self):
        reserva = Reserva(
            consumo=[{"valor": 5, "qnt": 2}, {"valor": 3, "qnt": 1}, {"valor": 4.5, "qnt": 1}]
        )
        self.assertEqual(reserva.calc_consumo(), 17.5, "Somatorio do consumo incorreto.")

unittest.main()