from dados.quarto import Quarto

class Reserva:
    def __init__(
        self,
        codr=None,
        data_r=None,
        check_in=None,
        check_out=None,
        desconto=None,
        status=None,
        quartos:list[Quarto]=[],
        consumo:list[dict]=[],
        codh=None
    ):
        self.__codr = codr
        self.__data_r = data_r
        self.__check_in = check_in
        self.__check_out = check_out
        self.__desconto = desconto
        self.__status = status
        self.__quartos = quartos
        self.__consumo = consumo
        self.__codh = codh

    def calc_consumo(self):
        total = 0
        for c in self.__consumo:
            total += (c["valor"] * c["qnt"])
        return total
    
    def diaria(self):
        total = 0
        for q in self.__quartos:
            total += q.get_valor()
        return total
    
    def subtotal(self):
        delta = self.__check_out - self.__check_in
        return self.diaria() * delta.days

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        else:
            return self.__codr == other.get_codr()
    
    # getters e setters

    def get_codr(self):
        return self.__codr
    
    def set_codr(self, codr):
        self.__codr = codr

    def get_data(self):
        return self.__data_r

    def get_check_in(self):
        return self.__check_in

    def set_check_in(self, check_in):
        self.__check_in = check_in

    def get_check_out(self):
        return self.__check_out
    
    def set_check_out(self, check_out):
        self.__check_out = check_out

    def get_desconto(self):
        return self.__desconto
    
    def set_desconto(self, desconto):
        self.__desconto = desconto

    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status

    def get_quartos(self):
        return self.__quartos
    
    def set_quartos(self, quartos):
        self.__quartos = quartos

    def get_codh(self):
        return self.__codh
    
    def set_codh(self, codh):
        self.__codh = codh

    def get_consumo(self):
        return self.__consumo

    def set_consumo(self, consumo):
        self.__consumo = consumo

