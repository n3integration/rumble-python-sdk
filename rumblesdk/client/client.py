import os
from http.client import HTTPConnection

from ..auth import AccessToken, Auth, Nil, OrgKey, ExportToken
from ..config import Client
from ..exception import AuthException

from .account import Account
from .export import Export
from .org import Org
from .releases import Releases


class ApiClient:
    def __init__(self, auth:Auth = Nil()):
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": Client.USER_AGENT_STRING
        }
        self.__auth = auth
        self.__auth.authorize(self.headers)
        self.__account = Account(self.headers)
        self.__export = Export(self.headers)
        self.__org = Org(self.headers)
        self.__releases = Releases(self.headers)
        self.init()

    def init(self):
        if os.getenv("RUMBLE_DEBUG", "").lower() == "true":
            import logging
            log = logging.getLogger('urllib3')
            log.setLevel(logging.DEBUG)

            stream = logging.StreamHandler()
            stream.setLevel(logging.DEBUG)
            log.addHandler(stream)
            HTTPConnection.debuglevel = 1

    def auth(self, auth: Auth):
        self.__auth = auth

    def account(self):
        raise Exception("not implemented")

    def export(self):
        raise Exception("not implemented")

    def org(self):
        if isinstance(self.__auth, OrgKey):
            return self.__org
        else:
            raise AuthException("Organization key is required")

    def releases(self):
        return self.__releases
