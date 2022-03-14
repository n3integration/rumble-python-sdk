import requests

from http import HTTPStatus
from pymarshaler.marshal import Marshal

from .http import *
from ..exception import ApiException


class Api:
    """
    Api provides a base implementation for API endpoints
    """

    def execute(self, method, url, headers, data=None):
        r = requests.request(method, url, headers=headers, data=data, allow_redirects=False, verify=True)
        if r.status_code == HTTPStatus.OK:
            if headers[CONTENT_TYPE].startswith(JSON):
                return r.json()
            elif headers[CONTENT_TYPE].startswith(CSV):
                return r.text
            return r.content
        elif r.status_code == HTTPStatus.NO_CONTENT:
            return None
        elif r.status_code == HTTPStatus.SEE_OTHER:
            return r.headers[LOCATION]
        raise ApiException(r.status_code, r.text)


def returns(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return _unmarshal(func(*args, **kwargs), klass)
        return wrapper
    return decorator


def _unmarshal(data, klass):
    marshal = Marshal(ignore_unknown_fields=True)
    if isinstance(data, list):
        values = []
        for value in data:
            values.append(marshal.unmarshal(klass, value))
        return values
    return marshal.unmarshal(klass, data)
