from unittest import TestCase
from use_cases.load_investments import LoadInvestments
from tests.use_cases.mocks.mock_investment_repo import MockInvestmentRepo
from tests.use_cases.mocks.mock_investment_presenter import MockInvestmentPresenter


class TestLoadTransactions(TestCase):
    def test_run(self):
        repo = MockInvestmentRepo('teste')
        load_transaction = LoadInvestments(repo, MockInvestmentPresenter())
        load_transaction.run('../files/LoadStocks_test_t.xlsx')
        lista = repo.get_investments_by_username()
        print(lista)
        print(lista[0].format_as_dict())
        self.assertEqual(2, len(lista))
