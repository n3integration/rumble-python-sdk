# coding: utf-8

"""
    Rumble API

    Rumble Network Discovery API  # noqa: E501

    OpenAPI spec version: 2.11.0
    Contact: support@rumble.run
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ScanOptions(object):
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
        'targets': 'str',
        'excludes': 'str',
        'scan_name': 'str',
        'scan_description': 'str',
        'scan_frequency': 'str',
        'scan_start': 'str',
        'scan_tags': 'str',
        'scan_grace_period': 'str',
        'agent': 'str',
        'rate': 'str',
        'max_host_rate': 'str',
        'passes': 'str',
        'max_attempts': 'str',
        'max_sockets': 'str',
        'max_group_size': 'str',
        'max_ttl': 'str',
        'tcp_ports': 'str',
        'tcp_excludes': 'str',
        'screenshots': 'str',
        'nameservers': 'str',
        'subnet_ping': 'str',
        'subnet_ping_net_size': 'str',
        'subnet_ping_sample_rate': 'str',
        'host_ping': 'str',
        'probes': 'str'
    }

    attribute_map = {
        'targets': 'targets',
        'excludes': 'excludes',
        'scan_name': 'scan-name',
        'scan_description': 'scan-description',
        'scan_frequency': 'scan-frequency',
        'scan_start': 'scan-start',
        'scan_tags': 'scan-tags',
        'scan_grace_period': 'scan-grace-period',
        'agent': 'agent',
        'rate': 'rate',
        'max_host_rate': 'max-host-rate',
        'passes': 'passes',
        'max_attempts': 'max-attempts',
        'max_sockets': 'max-sockets',
        'max_group_size': 'max-group-size',
        'max_ttl': 'max-ttl',
        'tcp_ports': 'tcp-ports',
        'tcp_excludes': 'tcp-excludes',
        'screenshots': 'screenshots',
        'nameservers': 'nameservers',
        'subnet_ping': 'subnet-ping',
        'subnet_ping_net_size': 'subnet-ping-net-size',
        'subnet_ping_sample_rate': 'subnet-ping-sample-rate',
        'host_ping': 'host-ping',
        'probes': 'probes'
    }

    def __init__(self, targets:str=None, excludes:str=None, scan_name:str=None, scan_description:str=None, scan_frequency:str=None, scan_start:str=None, scan_tags:str=None, scan_grace_period:str=None, agent:str=None, rate:str=None, max_host_rate:str=None, passes:str=None, max_attempts:str=None, max_sockets:str=None, max_group_size:str=None, max_ttl:str=None, tcp_ports:str=None, tcp_excludes:str=None, screenshots:str=None, nameservers:str=None, subnet_ping:str=None, subnet_ping_net_size:str=None, subnet_ping_sample_rate:str=None, host_ping:str=None, probes:str=None):  # noqa: E501
        """ScanOptions - a model defined in Swagger"""  # noqa: E501
        self._targets = None
        self._excludes = None
        self._scan_name = None
        self._scan_description = None
        self._scan_frequency = None
        self._scan_start = None
        self._scan_tags = None
        self._scan_grace_period = None
        self._agent = None
        self._rate = None
        self._max_host_rate = None
        self._passes = None
        self._max_attempts = None
        self._max_sockets = None
        self._max_group_size = None
        self._max_ttl = None
        self._tcp_ports = None
        self._tcp_excludes = None
        self._screenshots = None
        self._nameservers = None
        self._subnet_ping = None
        self._subnet_ping_net_size = None
        self._subnet_ping_sample_rate = None
        self._host_ping = None
        self._probes = None
        self.discriminator = None
        self.targets = targets
        if excludes is not None:
            self.excludes = excludes
        if scan_name is not None:
            self.scan_name = scan_name
        if scan_description is not None:
            self.scan_description = scan_description
        if scan_frequency is not None:
            self.scan_frequency = scan_frequency
        if scan_start is not None:
            self.scan_start = scan_start
        if scan_tags is not None:
            self.scan_tags = scan_tags
        if scan_grace_period is not None:
            self.scan_grace_period = scan_grace_period
        if agent is not None:
            self.agent = agent
        if rate is not None:
            self.rate = rate
        if max_host_rate is not None:
            self.max_host_rate = max_host_rate
        if passes is not None:
            self.passes = passes
        if max_attempts is not None:
            self.max_attempts = max_attempts
        if max_sockets is not None:
            self.max_sockets = max_sockets
        if max_group_size is not None:
            self.max_group_size = max_group_size
        if max_ttl is not None:
            self.max_ttl = max_ttl
        if tcp_ports is not None:
            self.tcp_ports = tcp_ports
        if tcp_excludes is not None:
            self.tcp_excludes = tcp_excludes
        if screenshots is not None:
            self.screenshots = screenshots
        if nameservers is not None:
            self.nameservers = nameservers
        if subnet_ping is not None:
            self.subnet_ping = subnet_ping
        if subnet_ping_net_size is not None:
            self.subnet_ping_net_size = subnet_ping_net_size
        if subnet_ping_sample_rate is not None:
            self.subnet_ping_sample_rate = subnet_ping_sample_rate
        if host_ping is not None:
            self.host_ping = host_ping
        if probes is not None:
            self.probes = probes

    @property
    def targets(self):
        """Gets the targets of this ScanOptions.  # noqa: E501


        :return: The targets of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this ScanOptions.


        :param targets: The targets of this ScanOptions.  # noqa: E501
        :type: str
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

    @property
    def excludes(self):
        """Gets the excludes of this ScanOptions.  # noqa: E501


        :return: The excludes of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._excludes

    @excludes.setter
    def excludes(self, excludes):
        """Sets the excludes of this ScanOptions.


        :param excludes: The excludes of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._excludes = excludes

    @property
    def scan_name(self):
        """Gets the scan_name of this ScanOptions.  # noqa: E501


        :return: The scan_name of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._scan_name

    @scan_name.setter
    def scan_name(self, scan_name):
        """Sets the scan_name of this ScanOptions.


        :param scan_name: The scan_name of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._scan_name = scan_name

    @property
    def scan_description(self):
        """Gets the scan_description of this ScanOptions.  # noqa: E501


        :return: The scan_description of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._scan_description

    @scan_description.setter
    def scan_description(self, scan_description):
        """Sets the scan_description of this ScanOptions.


        :param scan_description: The scan_description of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._scan_description = scan_description

    @property
    def scan_frequency(self):
        """Gets the scan_frequency of this ScanOptions.  # noqa: E501


        :return: The scan_frequency of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._scan_frequency

    @scan_frequency.setter
    def scan_frequency(self, scan_frequency):
        """Sets the scan_frequency of this ScanOptions.


        :param scan_frequency: The scan_frequency of this ScanOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["once", "hourly", "daily", "weekly", "monthly", "continuous"]  # noqa: E501
        if scan_frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `scan_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(scan_frequency, allowed_values)
            )

        self._scan_frequency = scan_frequency

    @property
    def scan_start(self):
        """Gets the scan_start of this ScanOptions.  # noqa: E501


        :return: The scan_start of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._scan_start

    @scan_start.setter
    def scan_start(self, scan_start):
        """Sets the scan_start of this ScanOptions.


        :param scan_start: The scan_start of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._scan_start = scan_start

    @property
    def scan_tags(self):
        """Gets the scan_tags of this ScanOptions.  # noqa: E501


        :return: The scan_tags of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._scan_tags

    @scan_tags.setter
    def scan_tags(self, scan_tags):
        """Sets the scan_tags of this ScanOptions.


        :param scan_tags: The scan_tags of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._scan_tags = scan_tags

    @property
    def scan_grace_period(self):
        """Gets the scan_grace_period of this ScanOptions.  # noqa: E501


        :return: The scan_grace_period of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._scan_grace_period

    @scan_grace_period.setter
    def scan_grace_period(self, scan_grace_period):
        """Sets the scan_grace_period of this ScanOptions.


        :param scan_grace_period: The scan_grace_period of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._scan_grace_period = scan_grace_period

    @property
    def agent(self):
        """Gets the agent of this ScanOptions.  # noqa: E501


        :return: The agent of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this ScanOptions.


        :param agent: The agent of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def rate(self):
        """Gets the rate of this ScanOptions.  # noqa: E501


        :return: The rate of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this ScanOptions.


        :param rate: The rate of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def max_host_rate(self):
        """Gets the max_host_rate of this ScanOptions.  # noqa: E501


        :return: The max_host_rate of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_host_rate

    @max_host_rate.setter
    def max_host_rate(self, max_host_rate):
        """Sets the max_host_rate of this ScanOptions.


        :param max_host_rate: The max_host_rate of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._max_host_rate = max_host_rate

    @property
    def passes(self):
        """Gets the passes of this ScanOptions.  # noqa: E501


        :return: The passes of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._passes

    @passes.setter
    def passes(self, passes):
        """Sets the passes of this ScanOptions.


        :param passes: The passes of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._passes = passes

    @property
    def max_attempts(self):
        """Gets the max_attempts of this ScanOptions.  # noqa: E501


        :return: The max_attempts of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the max_attempts of this ScanOptions.


        :param max_attempts: The max_attempts of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._max_attempts = max_attempts

    @property
    def max_sockets(self):
        """Gets the max_sockets of this ScanOptions.  # noqa: E501


        :return: The max_sockets of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_sockets

    @max_sockets.setter
    def max_sockets(self, max_sockets):
        """Sets the max_sockets of this ScanOptions.


        :param max_sockets: The max_sockets of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._max_sockets = max_sockets

    @property
    def max_group_size(self):
        """Gets the max_group_size of this ScanOptions.  # noqa: E501


        :return: The max_group_size of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_group_size

    @max_group_size.setter
    def max_group_size(self, max_group_size):
        """Sets the max_group_size of this ScanOptions.


        :param max_group_size: The max_group_size of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._max_group_size = max_group_size

    @property
    def max_ttl(self):
        """Gets the max_ttl of this ScanOptions.  # noqa: E501


        :return: The max_ttl of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_ttl

    @max_ttl.setter
    def max_ttl(self, max_ttl):
        """Sets the max_ttl of this ScanOptions.


        :param max_ttl: The max_ttl of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._max_ttl = max_ttl

    @property
    def tcp_ports(self):
        """Gets the tcp_ports of this ScanOptions.  # noqa: E501


        :return: The tcp_ports of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._tcp_ports

    @tcp_ports.setter
    def tcp_ports(self, tcp_ports):
        """Sets the tcp_ports of this ScanOptions.


        :param tcp_ports: The tcp_ports of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._tcp_ports = tcp_ports

    @property
    def tcp_excludes(self):
        """Gets the tcp_excludes of this ScanOptions.  # noqa: E501


        :return: The tcp_excludes of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._tcp_excludes

    @tcp_excludes.setter
    def tcp_excludes(self, tcp_excludes):
        """Sets the tcp_excludes of this ScanOptions.


        :param tcp_excludes: The tcp_excludes of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._tcp_excludes = tcp_excludes

    @property
    def screenshots(self):
        """Gets the screenshots of this ScanOptions.  # noqa: E501


        :return: The screenshots of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._screenshots

    @screenshots.setter
    def screenshots(self, screenshots):
        """Sets the screenshots of this ScanOptions.


        :param screenshots: The screenshots of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._screenshots = screenshots

    @property
    def nameservers(self):
        """Gets the nameservers of this ScanOptions.  # noqa: E501


        :return: The nameservers of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """Sets the nameservers of this ScanOptions.


        :param nameservers: The nameservers of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._nameservers = nameservers

    @property
    def subnet_ping(self):
        """Gets the subnet_ping of this ScanOptions.  # noqa: E501


        :return: The subnet_ping of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._subnet_ping

    @subnet_ping.setter
    def subnet_ping(self, subnet_ping):
        """Sets the subnet_ping of this ScanOptions.


        :param subnet_ping: The subnet_ping of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._subnet_ping = subnet_ping

    @property
    def subnet_ping_net_size(self):
        """Gets the subnet_ping_net_size of this ScanOptions.  # noqa: E501


        :return: The subnet_ping_net_size of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._subnet_ping_net_size

    @subnet_ping_net_size.setter
    def subnet_ping_net_size(self, subnet_ping_net_size):
        """Sets the subnet_ping_net_size of this ScanOptions.


        :param subnet_ping_net_size: The subnet_ping_net_size of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._subnet_ping_net_size = subnet_ping_net_size

    @property
    def subnet_ping_sample_rate(self):
        """Gets the subnet_ping_sample_rate of this ScanOptions.  # noqa: E501


        :return: The subnet_ping_sample_rate of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._subnet_ping_sample_rate

    @subnet_ping_sample_rate.setter
    def subnet_ping_sample_rate(self, subnet_ping_sample_rate):
        """Sets the subnet_ping_sample_rate of this ScanOptions.


        :param subnet_ping_sample_rate: The subnet_ping_sample_rate of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._subnet_ping_sample_rate = subnet_ping_sample_rate

    @property
    def host_ping(self):
        """Gets the host_ping of this ScanOptions.  # noqa: E501


        :return: The host_ping of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._host_ping

    @host_ping.setter
    def host_ping(self, host_ping):
        """Sets the host_ping of this ScanOptions.


        :param host_ping: The host_ping of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._host_ping = host_ping

    @property
    def probes(self):
        """Gets the probes of this ScanOptions.  # noqa: E501

        Optional probe list, otherwise all probes are used  # noqa: E501

        :return: The probes of this ScanOptions.  # noqa: E501
        :rtype: str
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        """Sets the probes of this ScanOptions.

        Optional probe list, otherwise all probes are used  # noqa: E501

        :param probes: The probes of this ScanOptions.  # noqa: E501
        :type: str
        """

        self._probes = probes

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
            elif value is not None:
                result[attr] = value
        if issubclass(ScanOptions, dict):
            for key, value in self.items():
                if value is not None:
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
        if not isinstance(other, ScanOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other