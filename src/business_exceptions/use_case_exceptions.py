from .bf_base_exception import BfBaseError


class EmptyDatabaseError(BfBaseError):
    message = "Banco de dados vazio."

    def __init__(self, message: str = None, *args) -> None:
        if message is not None:
            self.message = message
        super().__init__(self.message, *args)