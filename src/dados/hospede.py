from dados.reserva import Reserva

class Hospede:
    def __init__(
            self,
            codh=None,
            cpf=None,
            pnome=None,
            unome=None,
            cidade=None,
            endereco=None,
            telefone=None,
            reservas: list[Reserva] = [],
    ):
        self.__codh = codh
        self.__cpf = cpf
        self.__pnome = pnome
        self.__unome = unome
        self.__cidade = cidade
        self.__endereco = endereco
        self.__telefone = telefone
        self.__reservas = reservas

    def add_reserva(self, r:Reserva):
        self.__reservas.append(r)

    def remove_reserva(self, r:Reserva):
        self.__reservas.remove(r)

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.__codh == other.get_codh()

    # getters e setters

    def get_codh(self):
        return self.__codh
    
    def set_codh(self, codh):
        self.__codh = codh

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_nome(self):
        return self.__pnome
    
    def set_nome(self, nome):
        self.__pnome = nome

    def get_sobrenome(self):
        return self.__unome

    def set_sobrenome(self, sobrenome):
        self.__unome = sobrenome

    def get_cidade(self):
        return self.__cidade
    
    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_reservas(self):
        return self.__reservas
    
    def set_reservas(self, reservas):
        self.__reservas = reservas
