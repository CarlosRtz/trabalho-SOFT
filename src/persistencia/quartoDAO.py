from dados.quarto import Quarto
from exceptions import *
from persistencia.conexao import Conexao
from persistencia.frigobarDAO import FrigobarDAO
from persistencia.reservaDAO import ReservaDAO

class QuartoDAO:
    def __init__(self):
        self.__con = Conexao()
        self.__col = self.__con.collection("quarto")
        self.__fdao = FrigobarDAO()

    def __new_codq(self):
        try:
            res = self.__col.find({}, {"codq": 1, "_id": 0}).sort("codq", -1).limit(1)
            return res.next()["codq"] + 1
        except Exception:
            return 1
        
    def insert(self, q: Quarto):
        try:
            quarto = {
                "codq": self.__new_codq(),
                "tipo": q.get_tipo(),
                "valor": q.get_valor(),
                "banheiras": q.get_banheiras(),
                "descricao": q.get_descricao(),
                "camas": q.get_camas(),
                "frigobar": None
            }
            self.__col.insert_one(quarto)
        except Exception:
            raise InsertException

    def delete(self, q: Quarto):
        try:
            self.__col.delete_one({"codq": q.get_codq()})
        except Exception:
            raise DeleteException
        
    def update(self, q: Quarto):
        try:
            self.__col.update_one(
                {"codq": q.get_codq()},
                {
                    "$set":{
                        "tipo": q.get_tipo(),
                        "valor": q.get_valor(),
                        "banheiras": q.get_banheiras(),
                        "descricao": q.get_descricao(),
                        "camas": q.get_camas(),
                        "frigobar": None
                    }
                }
            )
        except Exception:
            raise UpdateException
        
    def __new_quarto(self, q):
        return Quarto(
            codq=q["codq"],
            tipo=q["tipo"],
            valor=q["valor"],
            banheiras=q["banheiras"],
            descricao=q["descricao"],
            camas=q["camas"],
            frigobar=self.__fdao.select_codq(q["codq"])
        )

    def select_all(self):
        try:
            result = self.__col.find()
            return [self.__new_quarto(r) for r in result]
        except Exception:
            raise SelectException

    def select_codq(self, codq):
        try:
            result = self.__col.find_one({"codq": codq})
            return self.__new_quarto(result)
        except Exception:
            raise SelectException
        
    def select_tipo(self, tipo):
        try:
            result = self.__col.find(
                {"tipo": tipo}
            )
            return [self.__new_quarto(q) for q in result]
        except Exception:
            raise SelectException

    def select_valor(self, valor):
        try:
            result = self.__col.find(
                {"valor": {"$lte": valor}}
            )
            return [self.__new_quarto(q) for q in result]
        except Exception:
            raise SelectException
