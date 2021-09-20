from unittest.mock import Mock

from use_cases import GetStocks


def test_run(mock_stock_repo, mock_stock):
    mock_presenter = Mock()
    use_case = GetStocks(mock_stock_repo, mock_presenter)
    use_case.run()
    response = mock_stock.format_as_dict()
    mock_presenter.respond.assert_called_with([response])
