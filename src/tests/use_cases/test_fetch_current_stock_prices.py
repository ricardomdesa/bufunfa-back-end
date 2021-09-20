from unittest.mock import Mock

from domain.entities import Stock
from use_cases import FetchCurrentStockPrices

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


def test_fetch_prices_run():

    stock_repo = Mock()
    config = {"get_stocks.return_value": MOCK_STOCKS_TO_UPDATE_FROM_REPO}
    stock_repo.configure_mock(**config)
    stock_api = Mock()
    config = {"get_stock_data.return_value": MOCK_STOCKS_UPDATED}
    stock_api.configure_mock(**config)
    presenter = Mock()

    FetchCurrentStockPrices(stock_repo, presenter, stock_api).run()
    stock_api.get_stock_data.assert_called_with(MOCK_STOCK_GET_DATA_API)
    stock_repo.update_all_by_code.assert_called_with(MOCK_STOCKS_UPDATED)
    presenter.respond.assert_called_with(3)
