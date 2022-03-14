from http import HTTPStatus

import requests

from ..config import API
from ..exception import ApiException


class Account:
    """
    Account contains, unauthenticated API endpoints
    """

    def __init__(self, headers):
        self.headers = headers
        self.baseUrl = f"{API.BASE_API_URL}/account"
