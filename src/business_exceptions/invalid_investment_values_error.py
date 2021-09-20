from business_exceptions import BfBaseError


class InvalidInvestmentValuesError(BfBaseError):
    message = "Valores de investimentos invalidos."

    def __init__(self, message: str = None, *args) -> None:
        if message is not None:
            self.message = message
        super().__init__(self.message, *args)