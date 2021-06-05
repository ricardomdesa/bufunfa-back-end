from use_cases.get_stocks import GetStocks
from tests.use_cases.mocks.stock_mock import STOCK_MOCK
from tests.use_cases.mocks.mock_stock_presenter import MockStockPresenter


class MockRepo:
    def __init__(self):
        self.__db = STOCK_MOCK

    def get_stocks_by_username(self):
        return self.__db


def test_run():
    mock_repo = MockRepo()
    use_case = GetStocks(mock_repo, MockStockPresenter())
    presenter_resp = use_case.run()
    assert presenter_resp == STOCK_MOCK

