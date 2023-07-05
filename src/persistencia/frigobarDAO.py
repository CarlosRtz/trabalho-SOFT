from dados.frigobar import Frigobar, Consumivel
from exceptions import *
from persistencia.conexao import Conexao

class FrigobarDAO:
    def __init__(self):
        self.__con = Conexao()
        self.__col = self.__con.collection("quarto")
    
    def __new_codf(self):
        try:
            result = self.__col.find({}, {"frigobar.codf": 1}).sort("frigobar.codf", -1).limit(1)
            return result["frigobar.codf"] + 1
        except Exception:
            return 1

    def insert(self, f: Frigobar):
        try:
            itens = [
                {"codi": 1, "nome": "Coca-cola 600ml", "marca": "Coca-Cola", "valor": 10.0, "qnt": 0},
                {"codi": 2,"nome": "Coca-cola zero 600ml", "marca": "Coca-Cola", "valor": 10.0, "qnt": 0},
                {"codi": 3,"nome": "Coca-cola 350ml", "marca": "Coca-Cola", "valor": 4.5, "qnt": 0},
                {"codi": 4,"nome": "Coca-cola zero 350ml", "marca": "Coca-Cola", "valor": 4.5, "qnt": 0},
                {"codi": 5,"nome": "Guaraná 600ml", "marca": "Guaraná Antarctica", "valor": 10.0, "qnt": 0},
                {"codi": 6,"nome": "Guaraná zero 600ml", "marca": "Guaraná Antarctica", "valor": 10.0, "qnt": 0},
                {"codi": 7,"nome": "Guaraná 350ml", "marca": "Guaraná Antarctica", "valor": 5.5, "qnt": 0},
                {"codi": 8,"nome": "Guaraná zero 350ml", "marca": "Guaraná Antarctica", "valor": 5.5, "qnt": 0},
                {"codi": 9,"nome": "Suco de laranja 250ml", "marca": "Del Valle", "valor": 4.5, "qnt": 0},
                {"codi": 10,"nome": "Suco de uva 250ml", "marca": "Del Valle", "valor": 4.5, "qnt": 0},
                {"codi": 11,"nome": "Suco de maracujá 250ml", "marca": "Del Valle", "valor": 4.5, "qnt": 0},
                {"codi": 12,"nome": "Água mineral 500ml", "marca": "Crystal", "valor": 4, "qnt": 0},
                {"codi": 13,"nome": "Água mineral com gás 500ml", "marca": "Crystal", "valor": 4, "qnt": 0}
            ]
            frigobar = {
                "codf": self.__new_codf(),
                "itens": itens
            }

            self.__col.update_one(
                {"codq": f.get_codq()},
                {"$set":{"frigobar": frigobar}}
            )
        except Exception:
            raise InsertException
        
    def delete(self, f: Frigobar):
        try:
            self.__col.update_one(
                {"codq": f.get_codq()},
                {"$set": {"frigobar": None}}
            )
        except Exception:
            raise DeleteException
        
    def update(self, f: Frigobar):
        try:
            itens = []
            for i, qnt in f.get_itens():
                itens.append({
                    "codi": i.get_nome(),
                    "nome": i.get_nome(),
                    "marca": i.get_marca(),
                    "valor": i.get_valor(),
                    "qnt": qnt
                })
            self.__col.update_one(
                {"codq": f.get_codq()},
                {
                    "$set":{
                        "frigobar.itens": itens
                    }
                }
            )
        except Exception:
            raise UpdateException
            
    def __new_frigobar(self, d):
        if d["frigobar"] == None: return None

        itens = []
        for i in d["frigobar"]["itens"]:
            itens.append(
                (
                    Consumivel(
                        codi=i["codi"],
                        nome=i["nome"],
                        marca=i["marca"],
                        valor=i["valor"]
                    ),
                    i["qnt"]
                )
            )

        f = Frigobar(
            codf=d["frigobar"]["codf"],
            codq=d["codq"],
            itens=itens
        )
        return f

    def select_all(self):
        try:
            result = self.__col.find(
                {"frigobar": {"$ne": None}},
                {"frigobar": 1, "codq": 1, "_id": 0}
            )
            return [self.__new_frigobar(d) for d in result]
        except Exception:
            raise SelectException

    def select_codf(self, codf):
        try:
            result = self.__col.find_one(
                {"frigobar.codf": codf},
                {"frigobar": 1, "codq": 1, "_id": 0}
            )
            return self.__new_frigobar(result)
        except Exception:
            raise SelectException

    def select_codq(self, codq):
        result = self.__col.find_one(
            {"codq": codq},
            {"frigobar": 1, "codq": 1, "_id": 0}
        )
        return self.__new_frigobar(result)