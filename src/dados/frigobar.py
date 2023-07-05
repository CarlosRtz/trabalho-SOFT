from dados.consumivel import Consumivel

class Frigobar:
    def __init__(
            self,
            codf=None,
            itens: list[tuple[Consumivel, int]] = [],
            codq=None
    ):
        self.__codf = codf
        self.__itens = itens
        self.__codq = codq

    def total_itens(self):
        total = 0
        for item, qnt in self.__itens:
            total += qnt
        return total

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.__codf == other.get_codf()
    
    ## getters e setters
    def get_codf(self):
        return self.__codf
    
    def set_codf(self, codf):
        self.__codf = codf

    def get_itens(self) -> list[tuple[Consumivel, int]]:
        return self.__itens
    
    def set_itens(self, itens):
        self.__itens = itens

    def get_codq(self):
        return self.__codq
    
    def set_codq(self, codq):
        self.__codq = codq