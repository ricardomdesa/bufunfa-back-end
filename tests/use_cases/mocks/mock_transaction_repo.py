
class MockTransactionRepo:

    def __init__(self, username: str):
        self.__transaction = None
        self.username = username

    def add_many(self, transaction: list):
        self.__transaction = transaction

    def get_all_transaction(self):
        return self.__transaction
