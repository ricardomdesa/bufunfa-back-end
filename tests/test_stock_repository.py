from repositories.stock_repository import StockRepository
from domain.stock import Stock
from unittest import TestCase


class TestStockRepository(TestCase):

    def test_add_many_stocks(self):
        stock_list = []

        stock_list.append(Stock('Teste1', 'TSTE1', 21.0))
        stock_list.append(Stock('Teste2', 'TSTE2', 9.65))

        StockRepository().add_many(stock_list)
        StockRepository().remove_by_code('TSTE2')

    def test_get_all_stocks(self):
        stock_list = StockRepository.get_all_stocks()
        StockRepository.remove_by_code('TSTE1')
        assert len(stock_list) == 1

    def test_get_by_code(self):
        stock_repo = StockRepository('ricardo')
        stock = stock_repo.get_stock_by_code('TRIS3.SA')
        self.assertEqual(Stock('Trisul', 'TRIS3.SA', 10.7).code, stock.code)

    def test_update_all_by_code(self):
        dict = {'BBDC3.SA': 22.01, 'TRIS3.SA': 10.7, 'RANI3.SA': 8.2}
        stock_repo = StockRepository('ricardo')
        stock_repo.update_all_by_code(dict)
        stock_from_repo = stock_repo.get_stock_by_code('TRIS3.SA')
        self.assertEqual(10.7, stock_from_repo.current_price)
