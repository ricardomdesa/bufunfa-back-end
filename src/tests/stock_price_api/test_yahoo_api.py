from stock_price_api.yahoo_api import YahooApiService
from tests.use_cases.mocks.mock_fetch_current_prices import MOCK_STOCKS_TO_UPDATE_FROM_REPO


def unused_test_yahoo_api():
    api = YahooApiService()
    stocks = list(map(lambda x: x.format_as_dict(), MOCK_STOCKS_TO_UPDATE_FROM_REPO))
    stocks_dict = api.get_stock_data(stocks)
    assert stocks_dict[0].get("stock_current_price") > 1
