from repositories.stock_repository import StockRepository
from domain.stock import Stock
from unittest import TestCase
from datetime import datetime, date
from tests.use_cases.mocks.mock_stock_repo import MockStockRepo


class TestStockRepository(TestCase):

    def test_add_many_stocks(self):
        stock_list = []

        stock_list.append(Stock('Teste1', 'TSTE1', 21.0).format_as_dict())
        stock_list.append(Stock('Teste2', 'TSTE2', 9.65).format_as_dict())

        stock_repo = StockRepository('teste')
        stock_repo.add_many(stock_list)
        stocks_from_repo = stock_repo.get_stocks()
        print('repo --', stocks_from_repo)
        print('list --', stock_list)
        assert stocks_from_repo == stock_list

    def test_get_all_stocks(self):
        stock_list = MockStockRepo.get_all_stocks()
        StockRepo.remove_by_code('TSTE1')
        assert len(stock_list) == 1

    def test_get_by_code(self):
        stock_repo = MockStockRepo('ricardo')
        stock = stock_repo.get_stock_by_code('TRIS3.SA')
        self.assertEqual(Stock('Trisul', 'TRIS3.SA', 10.7).code, stock.code)

    def test_update_all_by_code(self):
        dict_inicial = {'BBDC3.SA': 1, 'TRIS3.SA': 1, 'RANI3.SA': 1}
        dict_update = {'BBDC3.SA': 22.01, 'TRIS3.SA': 10.7, 'RANI3.SA': 8.2}

        stock_repo = MockStockRepo('teste')
        stock_repo.add_many(dict_inicial)
        stock_repo.update_all_by_code(dict_update, date.today())
        stock_from_repo = stock_repo.get_stock_by_code('TRIS3.SA')
        self.assertEqual(10.7, stock_from_repo.current_price)

    def test_update_all_by_code_date(self):
        stocks_inicial = [Stock('Brades', 'BBDC3.SA', 1), Stock('Tris', 'TRIS3.SA', 1)]
        stocks_update = [Stock('Brades', 'BBDC3.SA', 11), Stock('Tris', 'TRIS3.SA', 12)]

        stock_repo = MockStockRepo('teste')
        stock_repo.add_many(stocks_inicial)
        stock_repo.update_all_by_code(stocks_update, date.today())
        stock_from_repo = stock_repo.get_stock_by_code('TRIS3.SA')
        self.assertEqual(date.today(), stock_from_repo.last_update)

