class MockInvestmentPresenter:
    @staticmethod
    def respond(docs):
        return docs

    @staticmethod
    def respond_with_error():
        return b'{"message": "Erro ao buscar lista de investmentos"}'
