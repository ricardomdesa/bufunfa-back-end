class Stock:
    def __init__(self, name: str = "", code: str = "", current_price: float = 0.0, last_update=None):
        self.name = name
        self.code = code
        self.current_price = current_price
        self.last_update = last_update

    def set_last_update(self, data):
        self.last_update = data
        return self

    def set_current_price(self, price):
        self.current_price = price
        return self

    def format_as_dict(self):
        return {
            "stock_name": self.name,
            "stock_code": self.code,
            "stock_current_price": self.current_price,
            "stock_last_update": self.last_update,
        }
