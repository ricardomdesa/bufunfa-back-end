from unittest import TestCase
from use_cases.load_transactions import LoadTransactions
from tests.use_cases.mocks.mock_transaction_repo import MockTransactionRepo
from tests.use_cases.mocks.mock_transaction_presenter import MockTransactionPresenter


class TestLoadTransactions(TestCase):
    def test_run(self):
        repo = MockTransactionRepo('username')
        load_transaction = LoadTransactions(repo, MockTransactionPresenter())
        load_transaction.run('../files/LoadStocks_test_t.xlsx')
        lista = repo.get_all_transaction()
        self.assertEqual(2, len(lista))
