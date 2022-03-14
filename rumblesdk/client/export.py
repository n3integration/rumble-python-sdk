from urllib import parse

from .api import Api, GET, returns
from ..config import API
from ..exception import ApiException
from ..models.asset import Asset
from ..models.service import Service
from ..models.site import Site
from ..models.wireless import Wireless


class Export(Api):
    """
    Export contains authenticated API endpoints
    """

    def __init__(self, headers):
        self.headers = headers
        self.baseUrl = f"{API.BASE_API_URL}/export"

    @returns(Asset)
    def get_assets(self, criteria: str = None, fields: str = None):
        params = ""
        if criteria is not None or fields is not None:
            params = parse.urlencode({'fields': fields, 'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/org/assets.json?{params}", self.headers)

    def get_assets_csv(self, criteria: str = None):
        params = ""
        if criteria is not None:
            params = parse.urlencode({'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/org/assets.json?{params}", self.headers)

    def get_assets_xml(self, criteria: str = None):
        params = ""
        if criteria is not None:
            params = parse.urlencode({'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/org/assets.nmap.xml?{params}", self.headers)

    @returns(Service)
    def get_services(self, criteria: str = None, fields: str = None):
        params = ""
        if criteria is not None or fields is not None:
            params = parse.urlencode({'fields': fields, 'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/org/services.json?{params}", self.headers)

    def get_services_csv(self, criteria: str = None):
        params = ""
        if criteria is not None:
            params = parse.urlencode({'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/org/services.csv?{params}", self.headers)

    @returns(Site)
    def get_sites(self, criteria: str = None, fields: str = None):
        params = ""
        if criteria is not None or fields is not None:
            params = parse.urlencode({'fields': fields, 'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/org/sites.json?{params}", self.headers)

    def get_sites_csv(self):
        return self.execute(GET, f"{self.baseUrl}/org/sites.csv", self.headers)

    @returns(Wireless)
    def get_wireless(self, criteria: str = None, fields: str = None):
        params = ""
        if criteria is not None or fields is not None:
            params = parse.urlencode({'fields': fields, 'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/export/org/wireless.json?{params}", self.headers)

    def get_wireless_csv(self, criteria: str = None):
        params = ""
        if criteria is not None:
            params = parse.urlencode({'search': criteria})
        return self.execute(GET, f"{self.baseUrl}/export/org/wireless.csv?{params}", self.headers)

    def get_top_assets_csv(self, criteria: str = "types"):
        supported_criteria = ["hw", "os", "tags", "types"]
        if criteria not in supported_criteria:
            raise ApiException()
        return self.execute(GET, f"{self.baseUrl}/export/org/assets/top.{criteria}.csv", self.headers)

    def get_top_services_csv(self, criteria: str = "products"):
        supported_criteria = ["products", "protocols", "tcp", "udp"]
        if criteria not in supported_criteria:
            raise ApiException()
        return self.execute(GET, f"{self.baseUrl}/org/services/top.{criteria}.csv", self.headers)

    def get_subnet_utilization_csv(self, mask: str = None):
        params = ""
        if mask is not None:
            params = parse.urlencode({'mask': mask})
        return self.execute(GET, f"{self.baseUrl}/org/services/subnet.stats.csv?{params}", self.headers)
