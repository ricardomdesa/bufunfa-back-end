from .bf_base_exception import BfBaseError


class EmptyDatabaseError(BfBaseError):
    def __init__(self, message="Banco de dados vazio"):
        self.message = message
        super().__init__(self.message)
