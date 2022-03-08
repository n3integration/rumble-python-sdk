import requests

from http import HTTPStatus
from pymarshaler.marshal import Marshal

from ..exception import ApiException

DELETE = "delete"
GET = "get"
PATCH = "patch"
POST = "post"
PUT = "put"


class Api:
    """
    Api provides a base implementation for API endpoints
    """

    def execute(self, method, url, headers, data=None):
        r = requests.request(method, url, headers=headers, data=data, allow_redirects = False, verify=False)
        if r.status_code == HTTPStatus.OK:
            return r.json()
        elif r.status_code == HTTPStatus.NO_CONTENT:
            return None
        elif r.status_code == HTTPStatus.SEE_OTHER:
            return r.headers["Location"]
        raise ApiException(r.status_code, r.text)

    def unmarshal(self, data, klass):
        marshal = Marshal(ignore_unknown_fields=True)
        if isinstance(data, list):
            values = []
            for value in data:
                values.append(marshal.unmarshal(klass, value))
            return values
        return marshal.unmarshal(klass, data)
