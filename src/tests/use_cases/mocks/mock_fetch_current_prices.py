from domain.stock import Stock

MOCK_STOCKS_TO_UPDATE_FROM_REPO = [
    Stock(name="Btg Pactual", code="BPAC11.SA", current_price=1),
    Stock(name="Trisul", code="TRIS3.SA", current_price=1),
    Stock(name="Tupy", code="TUPY3.SA", current_price=1),
]

MOCK_STOCKS_UPDATED = [
    {
        "stock_name": "Btg Pactual",
        "stock_code": "BPAC11.SA",
        "stock_current_price": 10.0,
        "stock_last_update": "2021-07-01",
    },
    {"stock_name": "Trisul", "stock_code": "TRIS3.SA", "stock_current_price": 11.0, "stock_last_update": "2021-07-01"},
    {"stock_name": "Tupy", "stock_code": "TUPY3.SA", "stock_current_price": 22.0, "stock_last_update": "2021-07-01"},
]

MOCK_STOCK_GET_DATA_API = [
    {"stock_name": "Btg Pactual", "stock_code": "BPAC11.SA", "stock_current_price": 1, "stock_last_update": None},
    {"stock_name": "Trisul", "stock_code": "TRIS3.SA", "stock_current_price": 1, "stock_last_update": None},
    {"stock_name": "Tupy", "stock_code": "TUPY3.SA", "stock_current_price": 1, "stock_last_update": None},
]
