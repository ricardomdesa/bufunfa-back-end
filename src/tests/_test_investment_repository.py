from domain.investment import Investment
from repositories.investment_repository import InvestmentRepository

lista_invest_mock = [
    Investment("teste", "xp", "TEST3.SA", 20.0, 100).format_as_dict(),
    Investment("teste", "xp", "TEST4.SA", 19.0, 200).format_as_dict(),
]

lista_invest_update_mock = [Investment("teste", "xp", "TEST3.SA", 21.0, 200).format_as_dict()]


def test_add_many():
    invest_repo = InvestmentRepository("teste")
    invest_repo.add_many(lista_invest_mock)
    investments_size = len(invest_repo.get_investments_by_username())
    invest_repo.remove_all_by_username()
    assert 2 == investments_size


def test_get_investments_by_username():
    # prepare test inserting mock data
    invest_repo = InvestmentRepository("teste")
    invest_repo.add_many(lista_invest_mock)

    investments = invest_repo.get_investments_by_username()
    # clean db
    invest_repo.remove_all_by_username()
    assert {
        "username": "teste",
        "corretora": "xp",
        "codigo": "TEST3.SA",
        "valor_medio": 20.0,
        "quantidade": 100,
        "tipo": "acao",
        "valor_investido": 2000.0,
        "valor_investido_atual": None,
        "rendimento": None,
    } == investments[0].format_as_dict()


def test_update_all_by_username():
    # prepare test inserting mock data
    invest_repo = InvestmentRepository("teste")
    invest_repo.add_many(lista_invest_mock)

    invest_repo.update_all_by_username(lista_invest_update_mock)

    investment = invest_repo.get_investment_by_code("TEST3.SA")

    invest_repo.remove_all_by_username()

    assert {
        "username": "teste",
        "corretora": "xp",
        "codigo": "TEST3.SA",
        "valor_medio": 21.0,
        "quantidade": 200,
        "tipo": "acao",
        "valor_investido": 4200.0,
        "valor_investido_atual": None,
        "rendimento": None,
    } == investment[0].format_as_dict()


def test_remove_by_code():
    # prepare test inserting mock data
    invest_repo = InvestmentRepository("teste")
    invest_repo.add_many(lista_invest_mock)

    invest_repo.remove_by_code("TEST3.SA")

    investment = invest_repo.get_investment_by_code("TEST3.SA")

    invest_repo.remove_all_by_username()

    assert [] == investment
