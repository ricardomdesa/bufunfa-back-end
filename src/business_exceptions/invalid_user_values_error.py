from .bf_base_exception import BfBaseError


class InvalidUserValuesError(BfBaseError):
    message = "Valores de usuario invalidos."

    def __init__(self, message: str = None, *args) -> None:
        if message is not None:
            self.message = message
        super().__init__(self.message, *args)