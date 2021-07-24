import json

from fastapi import Response, status


class AuthenticationPresenter:
    @staticmethod
    def respond(access_token):
        response = Response()
        response.status_code = status.HTTP_200_OK
        response.body = json.dumps(dict(access_token=access_token, token_type="bearer")).encode("utf-8")
        return response

    @staticmethod
    def respond_with_error(message: str = "Incorrect username or password"):
        response = Response(headers={"WWW-Authenticate": "Bearer"})
        response.status_code = status.HTTP_401_UNAUTHORIZED
        response.body = json.dumps(dict(message=message)).encode("utf-8")
        return response
