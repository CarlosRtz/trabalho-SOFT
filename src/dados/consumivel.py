class Consumivel:
    def __init__(
        self,
        codi=None,
        nome=None,
        marca=None,
        valor=None,    
    ):
        self.__codi = codi
        self.__nome = nome
        self.__marca = marca
        self.__valor = valor

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.__codi == other.get_codi()

    def get_codi(self):
        return self.__codi
    
    def set_codi(self, codi):
        self.__codi = codi

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome 

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca

    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor