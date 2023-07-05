from dados import *
from persistencia import *

class Sistema:
    def __init__(self):
        self.__hdao = HospedeDAO()
        self.__rdao = ReservaDAO()
        self.__qdao = QuartoDAO()
        self.__fdao = FrigobarDAO()

    ## get hospedes
    def get_hospedes(self):
        return self.__hdao.select_all()
    
    def get_hospede(self, codh):
        return self.__hdao.select_codh(codh)
    
    def get_hospedes_cpf(self, cpf):
        return self.__hdao.select_cpf(cpf)
    
    def get_hospedes_nome(self, nome):
        return self.__hdao.select_nome(nome)
    
    ## get reservas
    def get_reservas(self):
        return self.__rdao.select_all()
    
    def get_reserva(self, codr):
        return self.__rdao.select_codr(codr)
    
    def get_reservas_cpf(self, cpf):
        return self.__rdao.select_cpf(cpf)
    
    def get_reservas_status(self, status):
        return self.__rdao.select_status(status)
    
    ## get quartos
    def get_quartos(self):
        return self.__qdao.select_all()
    
    def get_quarto(self, codq):
        return self.__qdao.select_codq(codq)
    
    def get_quartos_tipo(self, tipo):
        return self.__qdao.select_tipo(tipo)
    
    def get_quartos_valor(self, valor):
        return self.__qdao.select_valor(valor)
    
    ## get frigobar 
    def get_frigobares(self):
        return self.__fdao.select_all()
    
    def get_frigobar(self, codf):
        return self.__fdao.select_codf(codf)
    
    ## inserts
    def insert(self, _obj):
        if isinstance(_obj, Hospede):
            self.__hdao.insert(_obj)
        elif isinstance(_obj, Reserva):
            self.__rdao.insert(_obj)
        elif isinstance(_obj, Quarto):
            self.__qdao.insert(_obj)
        elif isinstance(_obj, Frigobar):
            self.__fdao.insert(Frigobar)

    ## deletes
    def delete(self, _obj):
        if isinstance(_obj, Hospede):
            self.__hdao.delete(_obj)
        elif isinstance(_obj, Reserva):
            self.__rdao.delete(_obj)
        elif isinstance(_obj, Quarto):
            self.__qdao.delete(_obj)
        elif isinstance(_obj, Frigobar):
            self.__fdao.delete(Frigobar)

    ## updates
    def update(self, _obj):
        if isinstance(_obj, Hospede):
            self.__hdao.update(_obj)
        elif isinstance(_obj, Reserva):
            self.__rdao.update(_obj)
        elif isinstance(_obj, Quarto):
            self.__qdao.update(_obj)
        elif isinstance(_obj, Frigobar):
            self.__fdao.update(Frigobar)   

    ## reserva de quartos
    def reservar_quarto(self, r: Reserva, q: Quarto):
        self.__rdao.reservar_quarto(r, q.get_codq())

    def liberar_quarto(self, r: Reserva, q: Quarto):
        self.__rdao.liberar_quarto(r.get_codr(), q.get_codq())     