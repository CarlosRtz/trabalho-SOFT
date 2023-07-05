from dados.frigobar import Frigobar

class Quarto:
    def __init__(
        self,
        codq=None,
        tipo=None,
        valor=None,
        banheiras=None,
        descricao=None,
        camas=None,
        frigobar : Frigobar = None
    ):
        self.__codq = codq
        self.__tipo = tipo
        self.__valor = valor
        self.__banheiras = banheiras
        self.__descricao = descricao
        self.__camas = camas
        self.__frigobar = frigobar

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.__codq == other.get_codq()
    # getters e setters

    def get_codq(self):
        return self.__codq
    
    def set_codq(self, codq):
        self.__codq = codq

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor

    def get_banheiras(self):
        return self.__banheiras
    
    def set_banheiras(self, banheiras):
        self.__banheiras = banheiras

    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_camas(self):
        return self.__camas
    
    def set_camas(self, camas):
        self.__camas = camas

    def get_frigobar(self):
        return self.__frigobar
    
    def set_frigobar(self, frigobar):
        self.__frigobar = frigobar