from pymongo import MongoClient

class Conexao:
    __instance = None
    __connection = None
    __db = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__connection = MongoClient("mongodb://localhost:27017")
            cls.__db = cls.__connection["teste"]
        return cls.__instance

    def collection(self, collection):
        return self.__db[collection]
    
    def close(self):
        self.__connection.close()