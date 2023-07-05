class InvalidFieldException(Exception):
    def __init__(self, field):
        self.message = f"Campo '{field}' inválido"
        super().__init__(self.message)

class InsertException(Exception):
    pass

class UpdateException(Exception):
    pass

class DeleteException(Exception):
    pass

class SelectException(Exception):
    pass

class ReservarQuartoException(Exception):
    pass

class LiberarQuartoException(Exception):
    pass