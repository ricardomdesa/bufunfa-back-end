from re import I
from src.domain.stock import Stock
from use_cases.get_stocks import GetStocks
from tests.use_cases.mocks.stock_mock import STOCK_MOCK
from tests.use_cases.mocks.mock_stock_presenter import MockStockPresenter
from tests.use_cases.mocks.mock_stock_repo import MockStockRepo


class MockRepo:
    def __init__(self):
        self.__db = STOCK_MOCK

    def get_stocks(self):
        return[Stock(stock['stock_name'],
          stock['stock_code'],
          stock["stock_current_price"], 
          stock['stock_last_update']) for stock in self.__db]


def test_run():
    mock_repo = MockStockRepo()
    mock_repo.set_username('teste')
    use_case = GetStocks(mock_repo, MockStockPresenter())
    presenter_resp = use_case.run()
    assert presenter_resp == [{
        'stock_name': 'teste',
        'stock_code': 'TEST3.SA',
        'stock_current_price': 22.6,
        'stock_last_update': '2021-05-22'
    }]

