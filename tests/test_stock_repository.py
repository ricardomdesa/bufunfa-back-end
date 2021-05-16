from repositories.stock_repository import StockRepository
from domain.stock import Stock


class TestStockRepository:

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