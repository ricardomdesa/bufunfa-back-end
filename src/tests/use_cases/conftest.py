from datetime import datetime
from unittest.mock import Mock

import pytest

from factories.InvestmentFactory import InvestmentFactory
from factories.StockFactory import StockFactory


@pytest.fixture
def mock_investment_repo():
    def _mock_investment_repo(first_param):
        # use the above params to mock and instantiate things
        mock_investment_repo = Mock()
        config = {
            "get_investments_by_username.return_value": [
                InvestmentFactory.build_from_doc_repo(doc) for doc in first_param
            ]
        }
        mock_investment_repo.configure_mock(**config)
        return mock_investment_repo

    # Pass this closure to the test
    yield _mock_investment_repo


@pytest.fixture
def mock_investment_repo_empty():
    mock_investment_repo = Mock()
    config = {"get_investments_by_username.return_value": []}
    mock_investment_repo.configure_mock(**config)
    return mock_investment_repo


@pytest.fixture
def mock_stock():
    return StockFactory.build_from_doc(
        {
            "stock_name": "teste",
            "stock_code": "TEST3.SA",
            "stock_current_price": 50.0,
            "stock_last_update": datetime.now(),
        }
    )


@pytest.fixture
def mock_stock_repo(mock_stock):
    mock_stock_repo = Mock()
    config = {
        "get_stock_by_code.return_value": mock_stock,
        "get_stocks.return_value": [mock_stock],
    }
    mock_stock_repo.configure_mock(**config)
    return mock_stock_repo


@pytest.fixture
def mock_result_presenter():
    return [
        {
            "username": "teste",
            "corretora": "xp",
            "codigo": "TEST3.SA",
            "valor_medio": 20.0,
            "quantidade": 100,
            "tipo": "acao",
            "valor_investido": 2000.0,
            "valor_investido_atual": 5000,
            "rendimento": 1.5,
            "current_stock_price": 50.0,
        }
    ]
