from unittest import TestCase
from use_cases.load_stocks import LoadStocks
from tests.use_cases.mocks.mock_stock_repo import MockStockRepo
from presenters.stock_presenter import StockPresenter


class TestLoadStocks(TestCase):
    def test_run(self):
        stock_loaded = b'{"message": "2 a\\u00e7\\u00f5es atualizadas com sucesso"}'
        load_stock = LoadStocks(MockStockRepo(), StockPresenter())
        respond = load_stock.run('../files/LoadStocks.xlsx')
        self.assertEqual(stock_loaded, respond.body)
