class MockStockPresenter:

    @staticmethod
    def respond(docs):
        return docs


    @staticmethod
    def respond_with_error(error):
        return error