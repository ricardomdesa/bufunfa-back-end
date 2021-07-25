from unittest.mock import Mock

from tests.use_cases.mocks.mock_fetch_current_prices import (
    MOCK_STOCK_GET_DATA_API,
    MOCK_STOCKS_TO_UPDATE_FROM_REPO,
    MOCK_STOCKS_UPDATED,
)
from use_cases.fetch_current_stock_prices import FetchCurrentStockPrices


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
