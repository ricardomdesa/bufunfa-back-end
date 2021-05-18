from unittest import TestCase
from repositories.stock_repository import StockRepository
from use_cases.fetch_current_stock_prices import FetchCurrentStockPrices


class TestFetchCurrentStockPrices(TestCase):
    def test_run(self):
        repo = StockRepository('ricardo')
        fetch = FetchCurrentStockPrices(repo)
        fetch.run()
        self.assertEqual(True, False)
