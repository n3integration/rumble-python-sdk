import copy
import json
import urllib.parse

from .api import Api, GET, POST, PATCH, PUT, DELETE
from ..config import API
from ..models.api_key import APIKey
from ..models.agent import Agent
from ..models.asset import Asset
from ..models.organization import Organization
from ..models.service import Service
from ..models.site import Site
from ..models.task import Task
from ..models.wireless import Wireless


class Org(Api):
    """
    Org contains organization API endpoints that require an organization key
    """

    def __init__(self, headers):
        self.headers = copy.deepcopy(headers)
        self.baseUrl = f"{API.BASE_API_URL}/org"

    def get(self):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}", self.headers), Organization)

    def update(self, org):
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}", self.headers, json.dumps(org)), Organization)

    def get_key(self):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/key", self.headers), APIKey)

    def delete_key(self):
        self.execute(DELETE, f"{self.baseUrl}/key", self.headers)

    def rotate_key(self):
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}/key/rotate", self.headers), APIKey)

    def get_explorer_list(self):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/agents", self.headers), Agent)

    def get_explorer(self, agent_id):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/agents/{agent_id}", self.headers), Agent)

    def delete_explorer(self, agent_id):
        return self.execute(DELETE, f"{self.baseUrl}/agents/{agent_id}", self.headers)

    def reassign_explorer(self, agent_id, site_id):
        data = {
            "site_id": site_id
        }
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}/agents/{agent_id}", self.headers, json.dumps(data)), Agent)

    def force_update_explorer(self, agent_id):
        self.execute(POST, f"{self.baseUrl}/agents/{agent_id}/update", self.headers)

    def get_site_list(self):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/sites", self.headers), Site)

    def create_site(self, site):
        return self.unmarshal(
            self.execute(PUT, f"{self.baseUrl}/sites", self.headers, json.dumps(site)), Site)

    def get_site(self, site_id):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/sites/{site_id}", self.headers), Site)

    def delete_site(self, site_id):
        self.execute(DELETE, f"{self.baseUrl}/sites/{site_id}", self.headers)

    def update_site(self, site):
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}/sites/{site.id}", self.headers, json.dumps(site)), Site)

    def import_scan(self, site_id, path):
        headers = copy.deepcopy(self.headers)
        headers["Content-Type"] = "application/octet-stream"
        with open(path, 'rb') as payload:
            return self.unmarshal(
                self.execute(PUT, f"{self.baseUrl}/sites/{site_id}/import", headers, payload), Task)

    def new_scan(self, site_id, opts):
        return self.unmarshal(
            self.execute(PUT, f"{self.baseUrl}/sites/{site_id}/scan", self.headers, json.dumps(opts)), Task)

    def get_asset_list(self, criteria=None):
        url = f"{self.baseUrl}/assets"
        if criteria is not None:
            url = f"{self.baseUrl}/assets?{urllib.parse.urlencode({'search': criteria})}"
        return self.unmarshal(
            self.execute(GET, url, self.headers), Asset)

    def get_asset(self, asset_id):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/assets/{asset_id}", self.headers), Asset)

    def delete_asset(self, asset_id):
        self.execute(DELETE, f"{self.baseUrl}/assets/{asset_id}", self.headers)

    def update_asset_comments(self, asset_id, comments):
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}/assets/{asset_id}/comments", self.headers, json.dumps(comments)),
            Asset)

    def update_asset_tags(self, asset_id, tags):
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}/assets/{asset_id}/tags", self.headers, json.dumps(tags)), Asset)

    def get_service_list(self, criteria=None):
        url = f"{self.baseUrl}/services"
        if criteria is not None:
            url = f"{self.baseUrl}/services?{urllib.parse.urlencode({'search': criteria})}"
        return self.unmarshal(
            self.execute(GET, url, self.headers), Service)

    def get_service(self, service_id):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/services/{service_id}", self.headers), Service)

    def delete_service(self, service_id):
        self.execute(DELETE, f"{self.baseUrl}/services/{service_id}", self.headers)

    def get_wireless_list(self, criteria=None):
        url = f"{self.baseUrl}/wireless"
        if criteria is not None:
            url = f"{self.baseUrl}/wireless?{urllib.parse.urlencode({'search': criteria})}"
        return self.unmarshal(
            self.execute(GET, url, self.headers), Wireless)

    def get_wireless(self, wireless_id):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/wireless/{wireless_id}", self.headers), Wireless)

    def delete_wireless(self, wireless_id):
        self.execute(DELETE, f"{self.baseUrl}/wireless/{wireless_id}", self.headers)

    def get_task_list(self, status=None, criteria=None):
        url = f"{self.baseUrl}/tasks"
        if criteria is not None or status is not None:
            url = f"{self.baseUrl}/tasks?{urllib.parse.urlencode({'status': status, 'search': criteria})}"
        return self.unmarshal(
            self.execute(GET, url, self.headers), Task)

    def get_task(self, task_id):
        return self.unmarshal(
            self.execute(GET, f"{self.baseUrl}/tasks/{task_id}", self.headers), Task)

    def update_task(self, task):
        return self.unmarshal(
            self.execute(PATCH, f"{self.baseUrl}/tasks/{task.id}", self.headers, json.dumps(task)))

    def get_task_data_link(self, task_id):
        return self.execute(GET, f"{self.baseUrl}/tasks/{task_id}/data", self.headers)

    def get_task_changes_link(self, task_id):
        return self.execute(GET, f"{self.baseUrl}/tasks/{task_id}/changes", self.headers)

    def get_task_log_link(self, task_id):
        return self.execute(GET, f"{self.baseUrl}/tasks/{task_id}/log", self.headers)

    def cancel_task(self, task_id):
        self.execute(POST, f"{self.baseUrl}/tasks/{task_id}/stop", self.headers)

    def update_task(self, task_id):
        self.execute(POST, f"{self.baseUrl}/tasks/{task_id}/hide", self.headers)
