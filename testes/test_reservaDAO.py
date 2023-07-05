import unittest
from dados import *
from persistencia import *

class TesteReservaDAOSelectAll(unittest.TestCase):
    def runTest(self):
        self.maxDiff= None
        rdao = ReservaDAO()
        reservas = [Reserva(codr=1), Reserva(codr=2), Reserva(codr=3)]
        self.assertListEqual(rdao.select_all(), reservas, "Reservas incorretas.")

class TestReservaDAOSelectCodr(unittest.TestCase):
    def runTest(self):
        rdao = ReservaDAO()
        r1 = Reserva(1)
        r2 = rdao.select_codr(1)
        self.assertEqual(r1, r2, "Reserva incorreta.")

class TestReservaDAOSelectStatus(unittest.TestCase):
    def test_status_pendente(self):
        rdao = ReservaDAO()
        r1 = Reserva(2)
        r2 = rdao.select_status("PENDENTE")[0]
        self.assertEqual(r1, r2, "Reserva incorreta.")

    def test_status_cancelado(self):
        rdao = ReservaDAO()
        r1 = Reserva(3)
        r2 = rdao.select_status("CANCELADO")[0]
        self.assertEqual(r1, r2, "Reserva incorreta.")

class TestReservaDAOSelectCpf(unittest.TestCase):
    def runTest(self):
        rdao = ReservaDAO()
        reservas = [Reserva(1), Reserva(2)]
        self.assertListEqual(rdao.select_cpf("00011100011"), reservas, "Reservas incorretas.")

unittest.main()