import pytest

from domain.stock import Stock
from stock_price_api.yahoo_api import YahooApiService


@pytest.fixture
def mock_stocks_to_update():
    return [
        Stock(name="Btg Pactual", code="BPAC11.SA", current_price=0),
        Stock(name="Trisul", code="TRIS3.SA", current_price=0),
        Stock(name="Tupy", code="TUPY3.SA", current_price=0),
    ]


def run_only_sometimes_test_yahoo_api(mock_stocks_to_update):
    api = YahooApiService()
    stocks = list(map(lambda x: x.format_as_dict(), mock_stocks_to_update))
    stocks_dict = api.get_stock_data(stocks)
    assert stocks_dict[0].get("stock_current_price") != 0
