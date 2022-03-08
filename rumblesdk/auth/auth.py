from ..exception import AuthException


class Auth:
    def authorize(self, headers):
        pass


class Nil(Auth):
    def authorize(self, headers):
        return


class OrgKey(Auth):
    def __init__(self, key):
        self.key = key

    def authorize(self, headers):
        if self.key is None:
            raise AuthException("Organization key is required")
        authorize(headers, f"Bearer {self.key}")


class ExportToken(Auth):
    def __init__(self, token):
        self.token = token

    def authorize(self, headers):
        if self.token is None:
            raise AuthException("Export token is required")
        authorize(headers, f"Bearer {self.token}")


class AccessToken(Auth):
    def __init__(self, token):
        self.token = token

    def authorize(self, headers):
        if self.token is None:
            raise AuthException("Access token is required")
        authorize(headers, f"Bearer {self.token}")


def authorize(headers, token):
    if token is not None:
        headers["Authorization"] = token
