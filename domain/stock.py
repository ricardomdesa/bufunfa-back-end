class Stock:
    def __init__(self, name: str, code: str, current_price: float):
        self.name = name
        self.code = code
        self.current_price = current_price

    def format_as_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'current_price': self.current_price
        }
