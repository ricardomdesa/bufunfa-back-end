import json
from fastapi import Response, status


class TransactionPresenter:

    @staticmethod
    def respond(docs):
        response = Response()
        response.status_code = status.HTTP_200_OK
        response.body = json.dumps(dict(message=f"{len(docs)} transacoes atualizadas com sucesso")).encode("utf-8")
        return response

    @staticmethod
    def respond_with_error(message: str = "Erro ao atualizar transacoes"):
        response = Response()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.body = json.dumps(dict(message=message)).encode("utf-8")
        return response