from unittest.mock import Mock, patch

import pytest

from business_exceptions import EmptyDatabaseError
from use_cases import GetInvestments

INVESTMENT_MOCK = [
    {
        "username": "teste",
        "corretora": "xp",
        "codigo": "TEST3.SA",
        "valor_medio": 20.0,
        "quantidade": 100,
        "tipo": "acao",
        "valor_investido": 2000.0,
        "valor_investido_atual": None,
        "rendimento": None,
    }
]


@pytest.mark.parametrize(["param_one"], [[INVESTMENT_MOCK]])
def test_get_investment(mock_investment_repo, param_one, mock_stock_repo, mock_result_presenter):
    mock_investment = mock_investment_repo(param_one)

    mock_presenter = Mock()
    uc = GetInvestments(mock_investment, mock_stock_repo, mock_presenter)
    uc.run()
    mock_presenter.respond.assert_called_with(mock_result_presenter)


@patch("logging.Logger.exception")
@pytest.mark.parametrize(["param_one"], [[list()]])
def test_get_investment_empty_db(mock, mock_investment_repo, param_one, mock_stock_repo):
    mock_investment = mock_investment_repo(param_one)
    mock_presenter = Mock()
    uc = GetInvestments(mock_investment, mock_stock_repo, mock_presenter)
    uc.run()
    exception = mock.call_args[0][0]
    assert isinstance(exception, EmptyDatabaseError)
