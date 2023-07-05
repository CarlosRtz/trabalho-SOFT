import unittest
from dados import *
from persistencia import *

class TestFrigobarDAOSelectAll(unittest.TestCase):
    def runTest(self):
        fdao = FrigobarDAO()
        frigobares = [Frigobar(codf=1), Frigobar(codf=2), Frigobar(codf=3)]
        self.assertListEqual(fdao.select_all(), frigobares, "Frigobares incorretos.")

class TestFrigobarDAOSelectCodf(unittest.TestCase):
    def runTest(self):
        fdao = FrigobarDAO()
        frigobar = Frigobar(codf=1)
        self.assertEqual(fdao.select_codf(1), frigobar, "Frigobar incorreto.")

unittest.main()