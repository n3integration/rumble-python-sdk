import os
from http.client import HTTPConnection

from .http import CONTENT_TYPE, USER_AGENT, ACCEPT, JSON
from ..auth import Auth, Nil, OrgKey, ExportToken, AccessToken
from ..config import Client
from ..exception import AuthException

from .account import Account
from .export import Export
from .org import Org
from .releases import Releases


class ApiClient:
    def __init__(self, auth: Auth = Nil()):
        self.headers = {
            ACCEPT: JSON,
            CONTENT_TYPE: JSON,
            USER_AGENT: Client.USER_AGENT_STRING
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
        if isinstance(self.__auth, AccessToken):
            return self.__account
        else:
            raise AuthException("Access token is required")

    def export(self):
        if isinstance(self.__auth, OrgKey) or isinstance(self.__auth, ExportToken):
            return self.__export
        else:
            raise AuthException("Export API requires an organization key or export token")

    def org(self):
        if isinstance(self.__auth, OrgKey):
            return self.__org
        else:
            raise AuthException("Organization key is required")

    def releases(self):
        return self.__releases
