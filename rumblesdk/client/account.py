import json
from urllib import parse

from .api import returns
from .http import GET, PUT, PATCH, DELETE, POST
from ..config import API
from ..models.agent import Agent
from ..models.api_key import APIKey
from ..models.credential import Credential
from ..models.event import Event
from ..models.group import Group
from ..models.group_mapping import GroupMapping
from ..models.group_post import GroupPost
from ..models.group_put import GroupPut
from ..models.license import License
from ..models.organization import Organization
from ..models.site import Site
from ..models.task import Task
from ..models.user import User


class Account:
    """
    Account contains, unauthenticated API endpoints
    """

    def __init__(self, headers):
        self.headers = headers
        self.baseUrl = f"{API.BASE_API_URL}/account"

    @returns(Organization)
    def get_orgs(self, search_criteria=None):
        params = ""
        if search_criteria is not None:
            params = parse.urlencode({'search': search_criteria})
        return self.execute(GET, f"{self.baseUrl}/orgs?{params}", self.headers)

    @returns(Organization)
    def create_org(self, org: Organization):
        return self.execute(PUT, f"{self.baseUrl}/orgs", self.headers, json.dumps(org))

    @returns(Organization)
    def get_org(self, org_id: str):
        return self.execute(GET, f"{self.baseUrl}/orgs/{org_id}", self.headers)

    @returns(Organization)
    def update_org(self, org: Organization):
        return self.execute(PATCH, f"{self.baseUrl}/orgs/{org.id}", self.headers)

    def remove_org(self, org_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/orgs/{org_id}", self.headers)

    def remove_export_token(self, org_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/orgs/{org_id}/exportToken", self.headers)

    @returns(APIKey)
    def rotate_export_token(self, org_id: str):
        return self.execute(PATCH, f"{self.baseUrl}/orgs/{org_id}/exportToken/rotate", self.headers)

    @returns(License)
    def get_license(self):
        return self.execute(GET, f"{self.baseUrl}/license", self.headers)

    @returns(Site)
    def get_sites(self):
        return self.execute(GET, f"{self.baseUrl}/sites", self.headers)

    @returns(Credential)
    def get_credentials(self):
        return self.execute(GET, f"{self.baseUrl}/credentials", self.headers)

    @returns(Credential)
    def create_credential(self, cred: Credential):
        return self.execute(PUT, f"{self.baseUrl}/credentials", self.headers, json.dumps(cred))

    @returns(Credential)
    def get_credential(self, cred_id: str):
        return self.execute(GET, f"{self.baseUrl}/credentials/{cred_id}", self.headers)

    @returns(Credential)
    def update_credential(self, cred: Credential):
        return self.execute(PATCH, f"{self.baseUrl}/credentials/{cred.id}", self.headers)

    def remove_credential(self, cred_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/credentials/{cred_id}", self.headers)

    @returns(APIKey)
    def get_keys(self):
        return self.execute(GET, f"{self.baseUrl}/keys", self.headers)

    @returns(APIKey)
    def create_key(self, key: APIKey):
        return self.execute(PUT, f"{self.baseUrl}/keys", self.headers, json.dumps(key))

    @returns(APIKey)
    def get_key(self, key_id: str):
        return self.execute(GET, f"{self.baseUrl}/keys/{key_id}", self.headers)

    @returns(APIKey)
    def rotate_key(self, key: APIKey):
        return self.execute(PATCH, f"{self.baseUrl}/keys/{key.id}", self.headers)

    def remove_key(self, key_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/keys/{key_id}", self.headers)

    @returns(Event)
    def get_events(self, search_criteria: str = None, fields: str = None):
        params = ""
        if search_criteria is not None or fields is not None:
            params = parse.urlencode({'fields': fields, 'search': search_criteria})
        return self.execute(GET, f"{self.baseUrl}/events.json?{params}", self.headers)

    @returns(Task)
    def get_tasks(self, search_criteria: str = None, fields: str = None):
        params = ""
        if search_criteria is not None or fields is not None:
            params = parse.urlencode({'fields': fields, 'search': search_criteria})
        return self.execute(GET, f"{self.baseUrl}/events.json?{params}", self.headers)

    @returns(Agent)
    def get_explorers(self, search_criteria: str = None):
        params = ""
        if search_criteria is not None:
            params = parse.urlencode({'search': search_criteria})
        return self.execute(GET, f"{self.baseUrl}/agents?{params}", self.headers)

    @returns(User)
    def get_users(self):
        return self.execute(GET, f"{self.baseUrl}/users", self.headers)

    @returns(User)
    def create_user(self, user: User):
        return self.execute(PUT, f"{self.baseUrl}/users", self.headers, json.dumps(user))

    @returns(User)
    def invite_user(self, user: User):
        return self.execute(PUT, f"{self.baseUrl}/users/invite", self.headers, json.dumps(user))

    @returns(User)
    def get_user(self, user_id: str):
        return self.execute(GET, f"{self.baseUrl}/users/{user_id}", self.headers)

    @returns(User)
    def update_user(self, user: APIKey):
        return self.execute(PATCH, f"{self.baseUrl}/users/{user.id}", self.headers)

    @returns(User)
    def reset_user_mfa(self, user: APIKey):
        return self.execute(PATCH, f"{self.baseUrl}/users/{user.id}/resetMFA", self.headers)

    @returns(User)
    def reset_user_lockout(self, user: APIKey):
        return self.execute(PATCH, f"{self.baseUrl}/users/{user.id}/resetLockout", self.headers)

    @returns(User)
    def reset_user_password(self, user: APIKey):
        return self.execute(PATCH, f"{self.baseUrl}/users/{user.id}/resetPassword", self.headers)

    def remove_user(self, user_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/users/{user_id}", self.headers)

    @returns(Group)
    def get_groups(self):
        return self.execute(GET, f"{self.baseUrl}/groups", self.headers)

    @returns(Group)
    def create_group(self, group: GroupPost):
        return self.execute(POST, f"{self.baseUrl}/groups", self.headers, json.dumps(group))

    @returns(Group)
    def get_group(self, group_id: str):
        return self.execute(GET, f"{self.baseUrl}/groups/{group_id}", self.headers)

    @returns(Group)
    def update_group(self, group: GroupPut):
        return self.execute(PUT, f"{self.baseUrl}/groups", self.headers, json.dumps(group))

    def remove_group(self, group_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/groups/{group_id}", self.headers)

    @returns(GroupMapping)
    def get_sso_groups(self):
        return self.execute(GET, f"{self.baseUrl}/sso/groups", self.headers)

    @returns(GroupMapping)
    def create_sso_group(self, group_mapping: GroupMapping):
        return self.execute(POST, f"{self.baseUrl}/sso/groups", self.headers, json.dumps(group_mapping))

    @returns(GroupMapping)
    def get_sso_group(self, group_mapping_id: str):
        return self.execute(GET, f"{self.baseUrl}/sso/groups/{group_mapping_id}", self.headers)

    @returns(GroupMapping)
    def update_sso_group(self, group_mapping: GroupMapping):
        return self.execute(PUT, f"{self.baseUrl}/sso/groups", self.headers, json.dumps(group_mapping))

    def remove_sso_group(self, group_mapping_id: str):
        return self.execute(DELETE, f"{self.baseUrl}/sso/groups/{group_mapping_id}", self.headers)
