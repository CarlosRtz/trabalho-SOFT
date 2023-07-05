import unittest
from persistencia import *
from dados import *

class TestHospedeDAOSelectAll(unittest.TestCase):
    def runTest(self):
        self.maxDiff = None
        hdao = HospedeDAO()
        hospedes = [
            Hospede(
                1, "00011100011", "Nome1", "Sobrenome1", "Cidade1", "Endereco1", "Telefone1"
            ),
            Hospede(
                2, "11100011100", "Nome2", "Sobrenome2", "Cidade2", "Endereco2", "Telefone2"
            ),
            Hospede(
                3, "01011100011", "Nome3", "Sobrenome3", "Cidade3", "Endereco3", "Telefone3"
            )
        ]
        self.assertListEqual(hdao.select_all(), hospedes, "Hospedes incorretos.")

class TestHospedeDAOSelectCodh(unittest.TestCase):
    def runTest(self):
        hdao = HospedeDAO()
        h1 = Hospede(
            codh=1, cpf="00011100011", pnome="Nome1", unome="Sobrenome1", cidade="Cidade1", endereco="Endereco1", telefone="Telefone1", reservas=[]
        )
        h2 = hdao.select_codh(1)
        self.assertEqual(h1, h2, "Hospede incorreto.")

class TestHospedeDAOSelectCpf(unittest.TestCase):
    def runTest(self):
        hdao = HospedeDAO()
        h1 = Hospede(
            codh=1, cpf="00011100011", pnome="Nome1", unome="Sobrenome1", cidade="Cidade1", endereco="Endereco1", telefone="Telefone1", reservas=[]
        )
        h2 = hdao.select_cpf("00011100011")[0]
        self.assertEqual(h1, h2, "Hospede incorreto.")

unittest.main()