class InvalidInvestmentValuesError(Exception):
    def __init__(self, message="Valores de investimentos invalidos."):
        self.message = message
