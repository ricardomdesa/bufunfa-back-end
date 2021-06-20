from domain.investment import Investment



class MockInvestmentRepo:

    def __init__(self):
        self.investments = []
        self.username = ""

    def set_username(self, username: str):
        self.username = username

    def set_db_data(self, data):
        self.investments = data[:]

    def add_many(self, transaction: list):
        self.investments = transaction

    def update_all_by_username(self, investments):
        self.investments = investments

    def get_investments_by_username(self):
        return [Investment(investment['username'],
                           investment['corretora'],
                           investment['codigo'],
                           investment['valor_medio'],
                           investment['quantidade'],
                           investment['tipo']
                           ) for investment in self.investments] if self.investments else []

    def get_investment_by_code(self):
        investment = self.investments[0]
        return Investment(investment['username'],
                          investment['corretora'],
                          investment['codigo'],
                          investment['valor_medio'],
                          investment['quantidade'],
                          investment['tipo']
                          )

    def remove_by_code(self):
        self.investments = list()

    def remove_all_by_username(self):
        self.investments = list()
