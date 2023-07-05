from dados.hospede import Hospede
from exceptions import *
from persistencia.conexao import Conexao
from persistencia.reservaDAO import ReservaDAO

class HospedeDAO:
    def __init__(self):
        self.__con = Conexao()
        self.__col = self.__con.collection("hospede")
        self.__rdao = ReservaDAO()

    def __new_codh(self):
        try:
            res = self.__col.find({}, {"codh": 1, "_id": 0}).sort("codh", -1).limit(1)
            return res.next()["codh"] + 1
        except Exception:
            return 1

    def insert(self, h: Hospede):
        try:
            hospede = {
                "codh": self.__new_codh(),
                "cpf": h.get_cpf(),
                "pnome": h.get_nome(),
                "unome": h.get_sobrenome(),
                "cidade": h.get_cidade(),
                "endereco": h.get_endereco(),
                "telefone": h.get_telefone(),
                "reservas": [],
            }
            self.__col.insert_one(hospede)
        except Exception:
            raise InsertException

    def delete(self, h: Hospede):
        try:
            self.__col.delete_one({"codh": h.get_codh()})
        except Exception:
            raise DeleteException

    def update(self, h: Hospede):
        self.__col.update_one(
            {"codh": h.get_codh()},
            {
                "$set":{
                    "cpf": h.get_cpf(),
                    "pnome": h.get_nome(),
                    "unome": h.get_sobrenome(),
                    "cidade": h.get_cidade(),
                    "endereco": h.get_endereco(),
                    "telefone": h.get_telefone(),
                }
            }
        )
    
    def __new_hospede(self, r):
        reservas = self.__rdao.select_codh(r["codh"])
        h = Hospede(
            codh=r["codh"],
            cpf=r["cpf"],
            pnome=r["pnome"],
            unome=r["unome"],
            cidade=r["cidade"],
            endereco=r["endereco"],
            telefone=r["telefone"],
            reservas=reservas,
        )
        return h

    def select_all(self):
        try:
            result = self.__col.find()
            return [self.__new_hospede(r) for r in result]
        except Exception:
            raise SelectException

    def select_codh(self, codh):
        try:
            return self.__new_hospede(self.__col.find_one({"codh": codh}))
        except Exception:
            raise SelectException

    def select_cpf(self, cpf):
        try:
            result = self.__col.find({"cpf":cpf})
            return [self.__new_hospede(r) for r in result]
        except Exception:
            raise SelectException

    def select_nome(self, nome):
        try:
            result = self.__col.find({"pnome": {"$regex": f"{nome}", "$options": "i"}})
            return [self.__new_hospede(r) for r in result]
        except Exception:
            raise SelectException