from unittest.mock import Mock, patch

import pandas
import pytest

from use_cases.load_investments import LoadInvestments


@pytest.fixture
def valid_invest_columns():
    valid_data = {
        "corretora": ["XP", "Inter", "Clear"],
        "codigo": ["BBDC3.SA", "TRIS3.SA", "RANI3.SA"],
        "quantidade": [800, 100, 200],
        "valor_medio": [11.0, 22.0, 33.0],
        "tipo": ["acao", "acao", "acao"],
    }
    return pandas.DataFrame(data=valid_data)


@pytest.fixture
def invalid_invest_columns():
    valid_data = {
        "corretora": ["XP", "Inter", "Clear"],
        "qtd": [800, 100, 200],
        "codigo": ["BBDC3.SA", "TRIS3.SA", "RANI3.SA"],
        "valor_medio": [11.0, 22.0, 33.0],
        "tipo": ["acao", "acao", "acao"],
    }
    return pandas.DataFrame(data=valid_data)


@pytest.fixture
def mock_invest_docs():
    return [
        {
            "username": "teste",
            "corretora": "XP",
            "codigo": "BBDC3.SA",
            "valor_medio": 11.0,
            "quantidade": 800,
            "tipo": "acao",
            "valor_investido": 8800.0,
            "valor_investido_atual": None,
            "rendimento": None,
            "current_stock_price": None,
        },
        {
            "username": "teste",
            "corretora": "Inter",
            "codigo": "TRIS3.SA",
            "valor_medio": 22.0,
            "quantidade": 100,
            "tipo": "acao",
            "valor_investido": 2200.0,
            "valor_investido_atual": None,
            "rendimento": None,
            "current_stock_price": None,
        },
        {
            "username": "teste",
            "corretora": "Clear",
            "codigo": "RANI3.SA",
            "valor_medio": 33.0,
            "quantidade": 200,
            "tipo": "acao",
            "valor_investido": 6600.0,
            "valor_investido_atual": None,
            "rendimento": None,
            "current_stock_price": None,
        },
    ]


@patch("pandas.read_csv")
def test_load_invest_pass(mock_csv: Mock, mock_invest_docs, valid_invest_columns):
    mock_csv.return_value = valid_invest_columns

    mock_invest_repo = Mock()
    mock_invest_repo.configure_mock(**{"username": "teste"})
    # mock_invest_repo.username = "teste"
    uc = LoadInvestments(mock_invest_repo, Mock())
    uc.run("any.csv")

    mock_csv.assert_called_with("any.csv", sep=",", dtype=str)
    mock_invest_repo.add_many.assert_called_with(mock_invest_docs)


@patch("pandas.read_csv")
def test_load_invest_invalid_csv(mock_csv: Mock, invalid_invest_columns):
    mock_csv.return_value = invalid_invest_columns

    mock_invest_repo = Mock()
    presenter = Mock()
    uc = LoadInvestments(mock_invest_repo, presenter)
    uc.run("any.csv")
    presenter.respond_with_error.assert_called_with("arquivo csv fora do padrao esperado")

    mock_csv.assert_called_with("any.csv", sep=",", dtype=str)
    mock_invest_repo.add_many.assert_not_called()
