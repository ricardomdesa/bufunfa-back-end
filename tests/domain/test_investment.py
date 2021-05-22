import pytest

from business_exceptions.invalid_investment_values_error import InvalidInvestmentValuesError
from domain.investment import Investment


def test_investment_domain_valid_values():
    investment = Investment("Teste", "XP", "TEST3.SA", 23.00, 100, "acao")
    assert {
               "username": "Teste",
               "corretora": "XP",
               "codigo": "TEST3.SA",
               "valor_medio": 23.00,
               "quantidade": 100,
               "tipo": "acao",
               "valor_investido": 2300.00,
               "valor_investido_atual": None,
               "rendimento": None
           } == investment.format_as_dict()


def test_investment_domain_invalid_code_size():
    with pytest.raises(InvalidInvestmentValuesError):
        Investment("Teste", "XP", "TES3.SA", 23.00, 100, "acao")


def test_investment_domain_invalid_code_ends():
    with pytest.raises(InvalidInvestmentValuesError):
        Investment("Teste", "XP", "TEST3", 23.00, 100, "acao")


def test_investment_domain_invalid_qtde_neg_value():
    with pytest.raises(InvalidInvestmentValuesError):
        Investment("Teste", "XP", "TEST3.SA", 23.00, -100, "acao")


def test_investment_domain_invalid_qtde_str_value():
    with pytest.raises(InvalidInvestmentValuesError):
        Investment("Teste", "XP", "TEST3.SA", 23.00, '100', "acao")


def test_investment_domain_invalid_avg_value_neg_value():
    with pytest.raises(InvalidInvestmentValuesError):
        Investment("Teste", "XP", "TEST3.SA", -23.00, 100, "acao")


def test_investment_domain_invalid_avg_value_str_value():
    with pytest.raises(InvalidInvestmentValuesError):
        Investment("Teste", "XP", "TEST3.SA", '23.00', 100, "acao")


def test_investment_domain_complementary_valor_investido_atual():
    investment = Investment("Teste", "XP", "TEST3.SA", 23.00, 100, "acao")
    investment.complement_with_stock_current_price(25.0)

    assert investment.format_as_dict()['valor_investido_atual'] == 2500.00


def test_investment_domain_complementary_valor_investido_atual():
    investment = Investment("Teste", "XP", "TEST3.SA", 10.00, 100, "acao")
    investment.complement_with_stock_current_price(12.55)
    print(investment.format_as_dict())

    assert investment.format_as_dict()['rendimento'] == 0.255
