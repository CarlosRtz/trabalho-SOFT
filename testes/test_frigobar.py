import unittest
from dados import *

class TestFrigobarTotalItens(unittest.TestCase):
    def runTest(self):
        frigobar = Frigobar(
            itens=[(None, 2), (None, 3), (None, 1), (None, 5)]
        )
        self.assertEqual(frigobar.total_itens(), 10, "Numero de itens incorreto.")

unittest.main()
