import json
from fastapi import Response, status


class StockPresenter:

    @staticmethod
    def respond(docs):
        response = Response()
        response.status_code = status.HTTP_200_OK
        response.body = json.dumps(dict(message=f"{len(docs)} ações atualizadas com sucesso")).encode("utf-8")
        return response

    @staticmethod
    def respond_with_error(message: str = "Erro ao atualizar stocks"):
        response = Response()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.body = json.dumps(dict(message=message)).encode("utf-8")
        return response
