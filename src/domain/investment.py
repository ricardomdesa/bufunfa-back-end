from business_exceptions.invalid_investment_values_error import InvalidInvestmentValuesError


class Investment:
    def __init__(
        self,
        username: str = "",
        corretora: str = "",
        codigo: str = "",
        valor_medio: float = 0.0,
        quantidade: int = 0,
        tipo: str = "acao",
        valor_investido_atual: float = None,
        rendimento: float = None,
    ):
        self.username = username
        self.corretora = corretora
        self.codigo = codigo
        self.valor_medio = valor_medio
        self.quantidade = quantidade
        self.tipo = tipo
        try:
            self.__valid_values = self.__validate_values()
            self.__valor_investido = self.__get_invested_value()
        except InvalidInvestmentValuesError as error:
            raise error
        self.__valor_investido_atual = valor_investido_atual
        self.__rendimento = rendimento
        self.__current_stock_price = None

    def __validate_values(self):
        is_stock_code_valid = self.validate_stock_code()
        is_average_value_valid = self.__validate_average_value()
        is_quantity_valid = self.__validate_quantity_value()
        if not is_stock_code_valid or not is_average_value_valid or not is_quantity_valid:
            raise InvalidInvestmentValuesError()
        return True

    def __get_invested_value(self):
        return self.valor_medio * self.quantidade

    def complement_with_stock_current_price(self, current_stock_price: float):
        self.__valor_investido_atual = round(self.quantidade * current_stock_price, 2)
        self.__rendimento = round((self.__valor_investido_atual / self.__valor_investido) - 1, 4)
        self.__current_stock_price = current_stock_price
        return self

    def validate_stock_code(self):
        valid_ends = self.codigo.endswith(".SA")
        valid_size = 8 <= len(self.codigo) <= 9
        return valid_ends and valid_size

    def __validate_average_value(self):
        return type(self.valor_medio) == float and self.valor_medio > 0.0

    def __validate_quantity_value(self):
        return type(self.quantidade) == int and self.quantidade > 0

    def format_as_dict(self):
        return {
            "username": self.username,
            "corretora": self.corretora,
            "codigo": self.codigo,
            "valor_medio": self.valor_medio,
            "quantidade": self.quantidade,
            "tipo": self.tipo,
            "valor_investido": self.__valor_investido,
            "valor_investido_atual": self.__valor_investido_atual,
            "rendimento": self.__rendimento,
            "current_stock_price": self.__current_stock_price,
        }
