import pytest
from unittest.mock import Mock, patch
import pandas
from datetime import datetime

from use_cases.load_stocks import LoadStocks


@pytest.fixture
def valid_stock_columns():
    valid_data = {
        "stock_name": ["Bradesco", "Trisul", "Irani"],
        "stock_code": ["BBDC3.SA", "TRIS3.SA", "RANI3.SA"],
        "stock_current_price": [1.0, 1.0, 1.0],
        "follow": ["sim", "sim", "sim"],
    }
    return pandas.DataFrame(data=valid_data)


@pytest.fixture
def invalid_stock_columns():
    valid_data = {
        "stock": ["Bradesco", "Trisul", "Irani"],
        "stock_code": ["BBDC3.SA", "TRIS3.SA", "RANI3.SA"],
        "stock_current_price": [1.0, 1.0, 1.0],
        "follow": ["sim", "sim", "sim"],
    }
    return pandas.DataFrame(data=valid_data)


@pytest.fixture
def mock_stock_docs():
    return [
        {
            "stock_name": "Bradesco",
            "stock_code": "BBDC3.SA",
            "stock_current_price": 1.0,
            "stock_last_update": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "stock_name": "Trisul",
            "stock_code": "TRIS3.SA",
            "stock_current_price": 1.0,
            "stock_last_update": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "stock_name": "Irani",
            "stock_code": "RANI3.SA",
            "stock_current_price": 1.0,
            "stock_last_update": datetime.now().strftime("%Y-%m-%d"),
        },
    ]


@patch("pandas.read_csv")
def test_load_stocks_pass(mock_csv: Mock, mock_stock_docs, valid_stock_columns):
    mock_csv.return_value = valid_stock_columns

    mock_stock_repo = Mock()
    uc = LoadStocks(mock_stock_repo, Mock())
    uc.run("any.csv")

    mock_csv.assert_called_with("any.csv", sep=",", dtype=str)
    mock_stock_repo.add_many.assert_called_with(mock_stock_docs)


@patch("pandas.read_csv")
def test_load_stocks_invalid_csv(mock_csv: Mock, invalid_stock_columns):
    mock_csv.return_value = invalid_stock_columns

    mock_stock_repo = Mock()
    presenter = Mock()
    uc = LoadStocks(mock_stock_repo, presenter)
    uc.run("any.csv")
    presenter.respond_with_error.assert_called_with("arquivo csv fora do padrao esperado")

    mock_csv.assert_called_with("any.csv", sep=",", dtype=str)
    mock_stock_repo.add_many.assert_not_called()
