class MockInvestmentPresenter:

    @staticmethod
    def respond(docs):
        return docs


    @staticmethod
    def respond_with_error():
        return 'error'