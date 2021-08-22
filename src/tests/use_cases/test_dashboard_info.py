from unittest.mock import Mock

import pytest

from use_cases.get_dashboard_info import GetDashboardInfo

INVESTMENT_MOCK_TWO = [
    {
        "username": "teste1",
        "corretora": "xp",
        "codigo": "TEST3.SA",
        "valor_medio": 20.0,
        "quantidade": 100,
        "tipo": "acao",
        "valor_investido": 2000.0,
        "valor_investido_atual": 2400,
        "rendimento": 0.2,
    },
    {
        "username": "teste1",
        "corretora": "xp",
        "codigo": "TEST4.SA",
        "valor_medio": 30.0,
        "quantidade": 100,
        "tipo": "acao",
        "valor_investido": 3000.0,
        "valor_investido_atual": 3300,
        "rendimento": 0.10,
    },
]


@pytest.mark.parametrize(["param_one"], [[INVESTMENT_MOCK_TWO]])
def test_dashboard_run(mock_investment_repo, param_one):
    mock_investment = mock_investment_repo(param_one)

    presenter = Mock()
    GetDashboardInfo(mock_investment, presenter).run()
    presenter.respond.assert_called_with([{"assets": 5700, "income_perc": 0.12, "income_value": 700.0}])


INVESTMENT_MOCK_TWO_CALC_EMPTY = [
    {
        "username": "teste1",
        "corretora": "xp",
        "codigo": "TEST3.SA",
        "valor_medio": 20.0,
        "quantidade": 100,
        "tipo": "acao",
        "valor_investido": 2000.0,
        "valor_investido_atual": None,
        "rendimento": None,
    },
    {
        "username": "teste1",
        "corretora": "xp",
        "codigo": "TEST4.SA",
        "valor_medio": 30.0,
        "quantidade": 100,
        "tipo": "acao",
        "valor_investido": 3000.0,
        "valor_investido_atual": None,
        "rendimento": None,
    },
]


@pytest.mark.parametrize(["param_one"], [[INVESTMENT_MOCK_TWO_CALC_EMPTY]])
def test_dashboard_run_without_current_price(mock_investment_repo, param_one):
    invest_repo = mock_investment_repo(param_one)

    presenter = Mock()
    GetDashboardInfo(invest_repo, presenter).run()
    presenter.respond.assert_called_with([{"assets": 0, "income_perc": 0, "income_value": 5000}])
