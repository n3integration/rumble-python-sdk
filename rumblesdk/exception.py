class ApiException(Exception):
    """
    General purpose exception raised from API calls
    """

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class AuthException(Exception):
    """
    General purpose exception raised when an authenticated API is called without credentials
    """

    def __init__(self, message: str = "Authentication is required"):
        self.message = message


class ClientApiException(Exception):
    """
    General purpose exception raised for invalid client API usage
    """

    def __init__(self, message: str):
        self.message = message
