class InvalidUserValuesError(Exception):
    def __init__(self, message="Valores de usuario invalidos."):
        self.message = message
