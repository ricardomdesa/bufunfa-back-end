import json
from fastapi import Response, status


class DashboardInfoPresenter:

    @staticmethod
    def respond(dashboard):
        response = Response()
        response.status_code = status.HTTP_200_OK
        response.body = json.dumps({'dashboard_info': dashboard}).encode("utf-8")
        return response

    @staticmethod
    def respond_with_error(message: str = "Erro ao buscar dashboard info"):
        response = Response()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.body = json.dumps(dict(message=message)).encode("utf-8")
        return response
