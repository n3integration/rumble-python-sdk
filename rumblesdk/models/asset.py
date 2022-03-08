# coding: utf-8

"""
    Rumble API

    Rumble Network Discovery API  # noqa: E501

    OpenAPI spec version: 2.10.0
    Contact: support@rumble.run
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Asset(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'organization_id': 'str',
        'site_id': 'str',
        'alive': 'bool',
        'first_seen': 'int',
        'last_seen': 'int',
        'detected_by': 'str',
        'type': 'str',
        'os': 'str',
        'os_version': 'str',
        'hw': 'str',
        'addresses': 'list[str]',
        'addresses_extra': 'list[str]',
        'macs': 'list[str]',
        'mac_vendors': 'list[str]',
        'names': 'list[str]',
        'domains': 'list[str]',
        'service_count': 'int',
        'service_count_tcp': 'int',
        'service_count_udp': 'int',
        'service_count_arp': 'int',
        'service_count_icmp': 'int',
        'lowest_ttl': 'int',
        'lowest_rtt': 'int',
        'last_agent_id': 'str',
        'last_task_id': 'str',
        'newest_mac': 'str',
        'newest_mac_vendor': 'str',
        'newest_mac_age': 'int',
        'comments': 'str',
        'service_ports_tcp': 'list[str]',
        'service_ports_udp': 'list[str]',
        'service_ports_protocols': 'list[str]',
        'service_ports_products': 'list[str]',
        'org_name': 'str',
        'site_name': 'str',
        'agent_name': 'str',
        'tags': 'dict(str, str)',
        'services': 'dict(str, dict(str, str))',
        'rtts': 'dict(str, object)',
        'credentials': 'dict(str, dict(str, bool))',
        'attributes': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'organization_id': 'organization_id',
        'site_id': 'site_id',
        'alive': 'alive',
        'first_seen': 'first_seen',
        'last_seen': 'last_seen',
        'detected_by': 'detected_by',
        'type': 'type',
        'os': 'os',
        'os_version': 'os_version',
        'hw': 'hw',
        'addresses': 'addresses',
        'addresses_extra': 'addresses_extra',
        'macs': 'macs',
        'mac_vendors': 'mac_vendors',
        'names': 'names',
        'domains': 'domains',
        'service_count': 'service_count',
        'service_count_tcp': 'service_count_tcp',
        'service_count_udp': 'service_count_udp',
        'service_count_arp': 'service_count_arp',
        'service_count_icmp': 'service_count_icmp',
        'lowest_ttl': 'lowest_ttl',
        'lowest_rtt': 'lowest_rtt',
        'last_agent_id': 'last_agent_id',
        'last_task_id': 'last_task_id',
        'newest_mac': 'newest_mac',
        'newest_mac_vendor': 'newest_mac_vendor',
        'newest_mac_age': 'newest_mac_age',
        'comments': 'comments',
        'service_ports_tcp': 'service_ports_tcp',
        'service_ports_udp': 'service_ports_udp',
        'service_ports_protocols': 'service_ports_protocols',
        'service_ports_products': 'service_ports_products',
        'org_name': 'org_name',
        'site_name': 'site_name',
        'agent_name': 'agent_name',
        'tags': 'tags',
        'services': 'services',
        'rtts': 'rtts',
        'credentials': 'credentials',
        'attributes': 'attributes'
    }

    def __init__(self, id:str=None, created_at:int=None, updated_at:int=None, organization_id:str=None, site_id:str=None, alive:bool=None, first_seen:int=None, last_seen:int=None, detected_by:str=None, type:str=None, os:str=None, os_version:str=None, hw:str=None, addresses:list[str]=None, addresses_extra:list[str]=None, macs:list[str]=None, mac_vendors:list[str]=None, names:list[str]=None, domains:list[str]=None, service_count:int=None, service_count_tcp:int=None, service_count_udp:int=None, service_count_arp:int=None, service_count_icmp:int=None, lowest_ttl:int=None, lowest_rtt:int=None, last_agent_id:str=None, last_task_id:str=None, newest_mac:str=None, newest_mac_vendor:str=None, newest_mac_age:int=None, comments:str=None, service_ports_tcp:list[str]=None, service_ports_udp:list[str]=None, service_ports_protocols:list[str]=None, service_ports_products:list[str]=None, org_name:str=None, site_name:str=None, agent_name:str=None, tags:dict=None, services:dict=None, rtts:dict=None, credentials:dict=None, attributes:dict=None):  # noqa: E501
        """Asset - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._organization_id = None
        self._site_id = None
        self._alive = None
        self._first_seen = None
        self._last_seen = None
        self._detected_by = None
        self._type = None
        self._os = None
        self._os_version = None
        self._hw = None
        self._addresses = None
        self._addresses_extra = None
        self._macs = None
        self._mac_vendors = None
        self._names = None
        self._domains = None
        self._service_count = None
        self._service_count_tcp = None
        self._service_count_udp = None
        self._service_count_arp = None
        self._service_count_icmp = None
        self._lowest_ttl = None
        self._lowest_rtt = None
        self._last_agent_id = None
        self._last_task_id = None
        self._newest_mac = None
        self._newest_mac_vendor = None
        self._newest_mac_age = None
        self._comments = None
        self._service_ports_tcp = None
        self._service_ports_udp = None
        self._service_ports_protocols = None
        self._service_ports_products = None
        self._org_name = None
        self._site_name = None
        self._agent_name = None
        self._tags = None
        self._services = None
        self._rtts = None
        self._credentials = None
        self._attributes = None
        self.discriminator = None
        self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if organization_id is not None:
            self.organization_id = organization_id
        if site_id is not None:
            self.site_id = site_id
        if alive is not None:
            self.alive = alive
        if first_seen is not None:
            self.first_seen = first_seen
        if last_seen is not None:
            self.last_seen = last_seen
        if detected_by is not None:
            self.detected_by = detected_by
        if type is not None:
            self.type = type
        if os is not None:
            self.os = os
        if os_version is not None:
            self.os_version = os_version
        if hw is not None:
            self.hw = hw
        if addresses is not None:
            self.addresses = addresses
        if addresses_extra is not None:
            self.addresses_extra = addresses_extra
        if macs is not None:
            self.macs = macs
        if mac_vendors is not None:
            self.mac_vendors = mac_vendors
        if names is not None:
            self.names = names
        if domains is not None:
            self.domains = domains
        if service_count is not None:
            self.service_count = service_count
        if service_count_tcp is not None:
            self.service_count_tcp = service_count_tcp
        if service_count_udp is not None:
            self.service_count_udp = service_count_udp
        if service_count_arp is not None:
            self.service_count_arp = service_count_arp
        if service_count_icmp is not None:
            self.service_count_icmp = service_count_icmp
        if lowest_ttl is not None:
            self.lowest_ttl = lowest_ttl
        if lowest_rtt is not None:
            self.lowest_rtt = lowest_rtt
        if last_agent_id is not None:
            self.last_agent_id = last_agent_id
        if last_task_id is not None:
            self.last_task_id = last_task_id
        if newest_mac is not None:
            self.newest_mac = newest_mac
        if newest_mac_vendor is not None:
            self.newest_mac_vendor = newest_mac_vendor
        if newest_mac_age is not None:
            self.newest_mac_age = newest_mac_age
        if comments is not None:
            self.comments = comments
        if service_ports_tcp is not None:
            self.service_ports_tcp = service_ports_tcp
        if service_ports_udp is not None:
            self.service_ports_udp = service_ports_udp
        if service_ports_protocols is not None:
            self.service_ports_protocols = service_ports_protocols
        if service_ports_products is not None:
            self.service_ports_products = service_ports_products
        if org_name is not None:
            self.org_name = org_name
        if site_name is not None:
            self.site_name = site_name
        if agent_name is not None:
            self.agent_name = agent_name
        if tags is not None:
            self.tags = tags
        if services is not None:
            self.services = services
        if rtts is not None:
            self.rtts = rtts
        if credentials is not None:
            self.credentials = credentials
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this Asset.  # noqa: E501


        :return: The id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Asset.


        :param id: The id of this Asset.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Asset.  # noqa: E501


        :return: The created_at of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Asset.


        :param created_at: The created_at of this Asset.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Asset.  # noqa: E501


        :return: The updated_at of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Asset.


        :param updated_at: The updated_at of this Asset.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def organization_id(self):
        """Gets the organization_id of this Asset.  # noqa: E501


        :return: The organization_id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Asset.


        :param organization_id: The organization_id of this Asset.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def site_id(self):
        """Gets the site_id of this Asset.  # noqa: E501


        :return: The site_id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Asset.


        :param site_id: The site_id of this Asset.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def alive(self):
        """Gets the alive of this Asset.  # noqa: E501


        :return: The alive of this Asset.  # noqa: E501
        :rtype: bool
        """
        return self._alive

    @alive.setter
    def alive(self, alive):
        """Sets the alive of this Asset.


        :param alive: The alive of this Asset.  # noqa: E501
        :type: bool
        """

        self._alive = alive

    @property
    def first_seen(self):
        """Gets the first_seen of this Asset.  # noqa: E501


        :return: The first_seen of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this Asset.


        :param first_seen: The first_seen of this Asset.  # noqa: E501
        :type: int
        """

        self._first_seen = first_seen

    @property
    def last_seen(self):
        """Gets the last_seen of this Asset.  # noqa: E501


        :return: The last_seen of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Asset.


        :param last_seen: The last_seen of this Asset.  # noqa: E501
        :type: int
        """

        self._last_seen = last_seen

    @property
    def detected_by(self):
        """Gets the detected_by of this Asset.  # noqa: E501


        :return: The detected_by of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._detected_by

    @detected_by.setter
    def detected_by(self, detected_by):
        """Sets the detected_by of this Asset.


        :param detected_by: The detected_by of this Asset.  # noqa: E501
        :type: str
        """

        self._detected_by = detected_by

    @property
    def type(self):
        """Gets the type of this Asset.  # noqa: E501


        :return: The type of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Asset.


        :param type: The type of this Asset.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def os(self):
        """Gets the os of this Asset.  # noqa: E501


        :return: The os of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this Asset.


        :param os: The os of this Asset.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def os_version(self):
        """Gets the os_version of this Asset.  # noqa: E501


        :return: The os_version of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this Asset.


        :param os_version: The os_version of this Asset.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def hw(self):
        """Gets the hw of this Asset.  # noqa: E501


        :return: The hw of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._hw

    @hw.setter
    def hw(self, hw):
        """Sets the hw of this Asset.


        :param hw: The hw of this Asset.  # noqa: E501
        :type: str
        """

        self._hw = hw

    @property
    def addresses(self):
        """Gets the addresses of this Asset.  # noqa: E501


        :return: The addresses of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Asset.


        :param addresses: The addresses of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    @property
    def addresses_extra(self):
        """Gets the addresses_extra of this Asset.  # noqa: E501


        :return: The addresses_extra of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses_extra

    @addresses_extra.setter
    def addresses_extra(self, addresses_extra):
        """Sets the addresses_extra of this Asset.


        :param addresses_extra: The addresses_extra of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._addresses_extra = addresses_extra

    @property
    def macs(self):
        """Gets the macs of this Asset.  # noqa: E501


        :return: The macs of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._macs

    @macs.setter
    def macs(self, macs):
        """Sets the macs of this Asset.


        :param macs: The macs of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._macs = macs

    @property
    def mac_vendors(self):
        """Gets the mac_vendors of this Asset.  # noqa: E501


        :return: The mac_vendors of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._mac_vendors

    @mac_vendors.setter
    def mac_vendors(self, mac_vendors):
        """Sets the mac_vendors of this Asset.


        :param mac_vendors: The mac_vendors of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._mac_vendors = mac_vendors

    @property
    def names(self):
        """Gets the names of this Asset.  # noqa: E501


        :return: The names of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this Asset.


        :param names: The names of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._names = names

    @property
    def domains(self):
        """Gets the domains of this Asset.  # noqa: E501


        :return: The domains of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this Asset.


        :param domains: The domains of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._domains = domains

    @property
    def service_count(self):
        """Gets the service_count of this Asset.  # noqa: E501


        :return: The service_count of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._service_count

    @service_count.setter
    def service_count(self, service_count):
        """Sets the service_count of this Asset.


        :param service_count: The service_count of this Asset.  # noqa: E501
        :type: int
        """

        self._service_count = service_count

    @property
    def service_count_tcp(self):
        """Gets the service_count_tcp of this Asset.  # noqa: E501


        :return: The service_count_tcp of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._service_count_tcp

    @service_count_tcp.setter
    def service_count_tcp(self, service_count_tcp):
        """Sets the service_count_tcp of this Asset.


        :param service_count_tcp: The service_count_tcp of this Asset.  # noqa: E501
        :type: int
        """

        self._service_count_tcp = service_count_tcp

    @property
    def service_count_udp(self):
        """Gets the service_count_udp of this Asset.  # noqa: E501


        :return: The service_count_udp of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._service_count_udp

    @service_count_udp.setter
    def service_count_udp(self, service_count_udp):
        """Sets the service_count_udp of this Asset.


        :param service_count_udp: The service_count_udp of this Asset.  # noqa: E501
        :type: int
        """

        self._service_count_udp = service_count_udp

    @property
    def service_count_arp(self):
        """Gets the service_count_arp of this Asset.  # noqa: E501


        :return: The service_count_arp of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._service_count_arp

    @service_count_arp.setter
    def service_count_arp(self, service_count_arp):
        """Sets the service_count_arp of this Asset.


        :param service_count_arp: The service_count_arp of this Asset.  # noqa: E501
        :type: int
        """

        self._service_count_arp = service_count_arp

    @property
    def service_count_icmp(self):
        """Gets the service_count_icmp of this Asset.  # noqa: E501


        :return: The service_count_icmp of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._service_count_icmp

    @service_count_icmp.setter
    def service_count_icmp(self, service_count_icmp):
        """Sets the service_count_icmp of this Asset.


        :param service_count_icmp: The service_count_icmp of this Asset.  # noqa: E501
        :type: int
        """

        self._service_count_icmp = service_count_icmp

    @property
    def lowest_ttl(self):
        """Gets the lowest_ttl of this Asset.  # noqa: E501


        :return: The lowest_ttl of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._lowest_ttl

    @lowest_ttl.setter
    def lowest_ttl(self, lowest_ttl):
        """Sets the lowest_ttl of this Asset.


        :param lowest_ttl: The lowest_ttl of this Asset.  # noqa: E501
        :type: int
        """

        self._lowest_ttl = lowest_ttl

    @property
    def lowest_rtt(self):
        """Gets the lowest_rtt of this Asset.  # noqa: E501


        :return: The lowest_rtt of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._lowest_rtt

    @lowest_rtt.setter
    def lowest_rtt(self, lowest_rtt):
        """Sets the lowest_rtt of this Asset.


        :param lowest_rtt: The lowest_rtt of this Asset.  # noqa: E501
        :type: int
        """

        self._lowest_rtt = lowest_rtt

    @property
    def last_agent_id(self):
        """Gets the last_agent_id of this Asset.  # noqa: E501


        :return: The last_agent_id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._last_agent_id

    @last_agent_id.setter
    def last_agent_id(self, last_agent_id):
        """Sets the last_agent_id of this Asset.


        :param last_agent_id: The last_agent_id of this Asset.  # noqa: E501
        :type: str
        """

        self._last_agent_id = last_agent_id

    @property
    def last_task_id(self):
        """Gets the last_task_id of this Asset.  # noqa: E501


        :return: The last_task_id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._last_task_id

    @last_task_id.setter
    def last_task_id(self, last_task_id):
        """Sets the last_task_id of this Asset.


        :param last_task_id: The last_task_id of this Asset.  # noqa: E501
        :type: str
        """

        self._last_task_id = last_task_id

    @property
    def newest_mac(self):
        """Gets the newest_mac of this Asset.  # noqa: E501


        :return: The newest_mac of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._newest_mac

    @newest_mac.setter
    def newest_mac(self, newest_mac):
        """Sets the newest_mac of this Asset.


        :param newest_mac: The newest_mac of this Asset.  # noqa: E501
        :type: str
        """

        self._newest_mac = newest_mac

    @property
    def newest_mac_vendor(self):
        """Gets the newest_mac_vendor of this Asset.  # noqa: E501


        :return: The newest_mac_vendor of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._newest_mac_vendor

    @newest_mac_vendor.setter
    def newest_mac_vendor(self, newest_mac_vendor):
        """Sets the newest_mac_vendor of this Asset.


        :param newest_mac_vendor: The newest_mac_vendor of this Asset.  # noqa: E501
        :type: str
        """

        self._newest_mac_vendor = newest_mac_vendor

    @property
    def newest_mac_age(self):
        """Gets the newest_mac_age of this Asset.  # noqa: E501


        :return: The newest_mac_age of this Asset.  # noqa: E501
        :rtype: int
        """
        return self._newest_mac_age

    @newest_mac_age.setter
    def newest_mac_age(self, newest_mac_age):
        """Sets the newest_mac_age of this Asset.


        :param newest_mac_age: The newest_mac_age of this Asset.  # noqa: E501
        :type: int
        """

        self._newest_mac_age = newest_mac_age

    @property
    def comments(self):
        """Gets the comments of this Asset.  # noqa: E501


        :return: The comments of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Asset.


        :param comments: The comments of this Asset.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def service_ports_tcp(self):
        """Gets the service_ports_tcp of this Asset.  # noqa: E501


        :return: The service_ports_tcp of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_ports_tcp

    @service_ports_tcp.setter
    def service_ports_tcp(self, service_ports_tcp):
        """Sets the service_ports_tcp of this Asset.


        :param service_ports_tcp: The service_ports_tcp of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._service_ports_tcp = service_ports_tcp

    @property
    def service_ports_udp(self):
        """Gets the service_ports_udp of this Asset.  # noqa: E501


        :return: The service_ports_udp of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_ports_udp

    @service_ports_udp.setter
    def service_ports_udp(self, service_ports_udp):
        """Sets the service_ports_udp of this Asset.


        :param service_ports_udp: The service_ports_udp of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._service_ports_udp = service_ports_udp

    @property
    def service_ports_protocols(self):
        """Gets the service_ports_protocols of this Asset.  # noqa: E501


        :return: The service_ports_protocols of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_ports_protocols

    @service_ports_protocols.setter
    def service_ports_protocols(self, service_ports_protocols):
        """Sets the service_ports_protocols of this Asset.


        :param service_ports_protocols: The service_ports_protocols of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._service_ports_protocols = service_ports_protocols

    @property
    def service_ports_products(self):
        """Gets the service_ports_products of this Asset.  # noqa: E501


        :return: The service_ports_products of this Asset.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_ports_products

    @service_ports_products.setter
    def service_ports_products(self, service_ports_products):
        """Sets the service_ports_products of this Asset.


        :param service_ports_products: The service_ports_products of this Asset.  # noqa: E501
        :type: list[str]
        """

        self._service_ports_products = service_ports_products

    @property
    def org_name(self):
        """Gets the org_name of this Asset.  # noqa: E501


        :return: The org_name of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this Asset.


        :param org_name: The org_name of this Asset.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def site_name(self):
        """Gets the site_name of this Asset.  # noqa: E501


        :return: The site_name of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this Asset.


        :param site_name: The site_name of this Asset.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

    @property
    def agent_name(self):
        """Gets the agent_name of this Asset.  # noqa: E501


        :return: The agent_name of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this Asset.


        :param agent_name: The agent_name of this Asset.  # noqa: E501
        :type: str
        """

        self._agent_name = agent_name

    @property
    def tags(self):
        """Gets the tags of this Asset.  # noqa: E501


        :return: The tags of this Asset.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Asset.


        :param tags: The tags of this Asset.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def services(self):
        """Gets the services of this Asset.  # noqa: E501


        :return: The services of this Asset.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Asset.


        :param services: The services of this Asset.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._services = services

    @property
    def rtts(self):
        """Gets the rtts of this Asset.  # noqa: E501


        :return: The rtts of this Asset.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._rtts

    @rtts.setter
    def rtts(self, rtts):
        """Sets the rtts of this Asset.


        :param rtts: The rtts of this Asset.  # noqa: E501
        :type: dict(str, object)
        """

        self._rtts = rtts

    @property
    def credentials(self):
        """Gets the credentials of this Asset.  # noqa: E501


        :return: The credentials of this Asset.  # noqa: E501
        :rtype: dict(str, dict(str, bool))
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Asset.


        :param credentials: The credentials of this Asset.  # noqa: E501
        :type: dict(str, dict(str, bool))
        """

        self._credentials = credentials

    @property
    def attributes(self):
        """Gets the attributes of this Asset.  # noqa: E501


        :return: The attributes of this Asset.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Asset.


        :param attributes: The attributes of this Asset.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Asset, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other