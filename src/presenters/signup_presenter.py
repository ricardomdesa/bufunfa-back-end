import json

from fastapi import Response, status


class SignUpPresenter:
    @staticmethod
    def respond(user):
        response = Response()
        response.status_code = status.HTTP_200_OK
        response.body = json.dumps(dict(message=f"usuario {user.username} adicionado com sucesso")).encode("utf-8")
        return response

    @staticmethod
    def respond_with_error(message: str = "Erro ao adicionar usuario"):
        response = Response()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.body = json.dumps(dict(message=message)).encode("utf-8")
        return response
