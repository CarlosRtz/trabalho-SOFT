import unittest
from dados import *
from persistencia import *

class TestQuartoDAOSelectAll(unittest.TestCase):
    def runTest(self):
        qdao = QuartoDAO()
        quartos = [Quarto(codq=1), Quarto(codq=2), Quarto(codq=3)]
        self.assertListEqual(qdao.select_all(), quartos, "Quartos incorretos.")

class TestQuartoDAOSelectCodq(unittest.TestCase):
    def runTest(self):
        qdao = QuartoDAO()
        quarto = Quarto(1)
        self.assertEqual(qdao.select_codq(1), quarto, "Quarto incorreto.")

class TestQuartoDAOSelectTipo(unittest.TestCase):
    def test_tipo_solteiro(self):
        qdao = QuartoDAO()
        q1 = Quarto(1)
        q2 = qdao.select_tipo("SOLTEIRO")[0]
        self.assertEqual(q1, q2, "Quarto incorreto.")
    
    def test_tipo_casal(self):
        qdao = QuartoDAO()
        q1 = Quarto(2)
        q2 = qdao.select_tipo("CASAL")[0]
        self.assertEqual(q1, q2, "Quarto incorreto.")

    def test_tipo_familia(self):
        qdao = QuartoDAO()
        q1 = Quarto(3)
        q2 = qdao.select_tipo("FAMILIA")[0]
        self.assertEqual(q1, q2, "Quarto incorreto.")

class TestQuartoDAOSelectValor(unittest.TestCase):
    def runTest(self):
        qdao = QuartoDAO()
        quartos = [Quarto(codq=1), Quarto(codq=2)]
        self.assertListEqual(qdao.select_valor(110.0), quartos, "Quartos incorretos.")

unittest.main()