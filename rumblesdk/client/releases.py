from .api import Api, GET
from ..config import API


class Releases(Api):
    """
    Releases contains public, unauthenticated API endpoints
    """

    def __init__(self, headers):
        self.headers = headers
        self.baseUrl = f"{API.BASE_API_URL}/releases"

    def get_agent_version(self):
        return self.execute(GET, f"{self.baseUrl}/agent/version", self.headers)

    def get_scanner_version(self):
        return self.execute(GET, f"{self.baseUrl}/scanner/version", self.headers)

    def get_platform_version(self):
        return self.execute(GET, f"{self.baseUrl}/platform/version", self.headers)
