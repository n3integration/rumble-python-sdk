class ApiException(Exception):
    """
    General purpose exception raised from API calls
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message


class AuthException(Exception):
    """
    General purpose exception raised when an authenticated API is called without credentials
    """

    def __init__(self, message="Authentication is required"):
        self.message = message
