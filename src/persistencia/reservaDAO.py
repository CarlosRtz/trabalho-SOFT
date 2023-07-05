from dados.reserva import Reserva
from exceptions import *
from persistencia.conexao import Conexao
from datetime import datetime, timedelta

class ReservaDAO:
    def __init__(self):
        self.__con = Conexao()
        self.__col = self.__con.collection("hospede")

    def __new_codr(self):
        try:
            result = self.__col.aggregate(
                [
                    {"$unwind": "$reservas"},
                    {"$project": {"codr": {"$max": "$reservas.codr"}}},
                    {"$sort": {"codr": -1}},
                    {"$limit": 1}
                ]
            )
            return result.next()["codr"] + 1
        except Exception:
            return 1

    def insert(self, r: Reserva):
        try:
            codr = self.__new_codr()
            reserva = {
                "codr": codr,
                "data_r": datetime.now(),
                "check_in": r.get_check_in(),
                "check_out": r.get_check_out(),
                "desconto": r.get_desconto(),
                "status": "PENDENTE",
                "quartos": [],
                "consumo": []
            }
            self.__col.update_one(
                {"codh": r.get_codh()},
                {"$push":{"reservas": reserva}}
            )
        except Exception:
            raise InsertException

    def delete(self, r: Reserva):
        try:
            self.__col.update_one(
                {"codh": r.get_codh()},
                {"$pull": {"reservas": {"codr": r.get_codr()}}}
            )
        except Exception:
            raise DeleteException

    def update(self, r: Reserva):
        try:
            self.__col.update_one(
                {
                    "codh": r.get_codh(),
                    "reservas": {"$elemMatch": {"codr": r.get_codr()}}
                },
                {
                    "$set":{
                        "reservas.$.check_in": r.get_check_in(),
                        "reservas.$.check_out": r.get_check_out(),
                        "reservas.$.desconto": r.get_desconto(),
                        "reservas.$.status": r.get_status()
                    }
                }
            )
        except Exception:
            raise UpdateException

    # método para verificar se o quarto já está reservado em uma data
    def __check_data(self, r: Reserva, codq):
        try:
            res = self.__col.aggregate(
                [
                    {"$unwind": "$reservas"},
                    {"$project": {"reserva": "$reservas"}},
                    {
                        "$match": {
                            "reserva.quartos": codq,
                            "$or": [{"reserva.status": "PENDENTE"}, {"reserva.status": "CONFIRMADO"}],
                            "$and": [{"reserva.check_in": {"$lt": r.get_check_out()}}, {"reserva.check_out": {"$gt": r.get_check_in()}}]
                        }
                    },
                    {"$count": "c"}
                ]
            )
            return res.next()["c"]
        except Exception:
            return 0
        
    def reservar_quarto(self, r: Reserva, codq):
        if self.__check_data(r, codq) == 0:
            self.__col.update_one(
                {"reservas": {"$elemMatch": {"codr": r.get_codr()}}},
                {
                    "$push":{"reservas.$.quartos": codq}
                }
            )
        else:
            raise ReservarQuartoException

    def liberar_quarto(self, codr, codq):
        try:
            self.__col.update_one(
                {"reservas": {"$elemMatch": {"codr": codr}}},
                {
                    "$pull":{"reservas.$.quartos": codq}
                }
            )
        except Exception:
            raise LiberarQuartoException
        
    def __new_reserva(self, r, codh):
        return Reserva(
            codr=r["codr"],
            data_r=r["data_r"],
            check_in=r["check_in"],
            check_out=r["check_out"],
            desconto=r["desconto"],
            status=r["status"],
            quartos=r["quartos"],
            consumo=r["consumo"],
            codh=codh
        )

    def select_all(self) -> list[Reserva]:
        try:
            result = self.__col.find(
                {},
                {"reservas": 1, "codh": 1}
            )
            reservas = []
            for rs in result:
                reservas += [self.__new_reserva(r, rs["codh"]) for r in rs["reservas"]]
            return reservas
        except Exception:
            raise SelectException

    def select_codr(self, codr):
        try:
            result = self.__col.find_one(
                {"reservas.codr": codr},
                {"reservas": {"$elemMatch": {"codr": codr}}, "codh": 1}
            )
            r = result["reservas"][0]
            return self.__new_reserva(r, result["codh"])
        except Exception:
            raise SelectException

    def select_cpf(self, cpf):
        try:
            result = self.__col.find(
                {"cpf": cpf},
                {"reservas": 1, "codh": 1}
            )
            reservas = []
            for rs in result:
                if "reservas" in rs:
                    reservas += [self.__new_reserva(r, rs["codh"]) for r in rs["reservas"]]
            return reservas
        except Exception:
            raise SelectException

    def select_status(self, status):
        try:
            result = self.__col.find(
                {},
                {"reservas": {"$elemMatch": {"status": status}}, "codh": 1}
            )
            reservas = []
            for rs in result:
                if "reservas" in rs:
                    reservas += [self.__new_reserva(r, rs["codh"]) for r in rs["reservas"]]
            return reservas
        except Exception:
            raise SelectException
        
    def select_codh(self, codh):
        result = self.__col.find_one(
            {"codh": codh},
            {"reservas": 1, "codh": 1}
        )
        reservas = [self.__new_reserva(r, result["codh"]) for r in result["reservas"]]
        return reservas

