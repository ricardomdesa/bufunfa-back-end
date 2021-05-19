from unittest import TestCase
from repositories.stock_repository import StockRepository
from presenters.fetch_stock_prices_presenter import FetchStockPricesPresenter
from use_cases.fetch_current_stock_prices import FetchCurrentStockPrices
from fastapi import Response, status


class TestFetchCurrentStockPrices(TestCase):
    def test_run(self):
        repo = StockRepository('ricardo')
        presenter = FetchStockPricesPresenter()
        use_case = FetchCurrentStockPrices(repo, presenter)
        response = use_case.run()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
