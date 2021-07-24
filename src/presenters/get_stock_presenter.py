import json

from fastapi import Response, status


class GetStockPresenter:
    @staticmethod
    def respond(stocks):
        response = Response()
        response.status_code = status.HTTP_200_OK
        response.body = json.dumps({"stock_list": stocks}).encode("utf-8")
        return response

    @staticmethod
    def respond_with_error(message: str = "Erro ao buscar lista de ações"):
        response = Response()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.body = json.dumps(dict(message=message)).encode("utf-8")
        return response
