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

class APIKey(object):
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
        'client_id': 'str',
        'organization_id': 'str',
        'created_at': 'int',
        'created_by': 'str',
        'comment': 'str',
        'last_used_at': 'int',
        'last_used_ip': 'str',
        'last_used_ua': 'str',
        'counter': 'int',
        'usage_today': 'int',
        'usage_limit': 'int',
        'token': 'str',
        'inactive': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'client_id': 'client_id',
        'organization_id': 'organization_id',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'comment': 'comment',
        'last_used_at': 'last_used_at',
        'last_used_ip': 'last_used_ip',
        'last_used_ua': 'last_used_ua',
        'counter': 'counter',
        'usage_today': 'usage_today',
        'usage_limit': 'usage_limit',
        'token': 'token',
        'inactive': 'inactive',
        'type': 'type'
    }

    def __init__(self, id:str=None, client_id:str=None, organization_id:str=None, created_at:int=None, created_by:str=None, comment:str=None, last_used_at:int=None, last_used_ip:str=None, last_used_ua:str=None, counter:int=None, usage_today:int=None, usage_limit:int=None, token:str=None, inactive:bool=None, type:str=None):  # noqa: E501
        """APIKey - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._client_id = None
        self._organization_id = None
        self._created_at = None
        self._created_by = None
        self._comment = None
        self._last_used_at = None
        self._last_used_ip = None
        self._last_used_ua = None
        self._counter = None
        self._usage_today = None
        self._usage_limit = None
        self._token = None
        self._inactive = None
        self._type = None
        self.discriminator = None
        self.id = id
        if client_id is not None:
            self.client_id = client_id
        if organization_id is not None:
            self.organization_id = organization_id
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if comment is not None:
            self.comment = comment
        if last_used_at is not None:
            self.last_used_at = last_used_at
        if last_used_ip is not None:
            self.last_used_ip = last_used_ip
        if last_used_ua is not None:
            self.last_used_ua = last_used_ua
        if counter is not None:
            self.counter = counter
        if usage_today is not None:
            self.usage_today = usage_today
        if usage_limit is not None:
            self.usage_limit = usage_limit
        if token is not None:
            self.token = token
        if inactive is not None:
            self.inactive = inactive
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this APIKey.  # noqa: E501


        :return: The id of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this APIKey.


        :param id: The id of this APIKey.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def client_id(self):
        """Gets the client_id of this APIKey.  # noqa: E501


        :return: The client_id of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this APIKey.


        :param client_id: The client_id of this APIKey.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def organization_id(self):
        """Gets the organization_id of this APIKey.  # noqa: E501


        :return: The organization_id of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this APIKey.


        :param organization_id: The organization_id of this APIKey.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def created_at(self):
        """Gets the created_at of this APIKey.  # noqa: E501


        :return: The created_at of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this APIKey.


        :param created_at: The created_at of this APIKey.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this APIKey.  # noqa: E501


        :return: The created_by of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this APIKey.


        :param created_by: The created_by of this APIKey.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def comment(self):
        """Gets the comment of this APIKey.  # noqa: E501


        :return: The comment of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this APIKey.


        :param comment: The comment of this APIKey.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def last_used_at(self):
        """Gets the last_used_at of this APIKey.  # noqa: E501


        :return: The last_used_at of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._last_used_at

    @last_used_at.setter
    def last_used_at(self, last_used_at):
        """Sets the last_used_at of this APIKey.


        :param last_used_at: The last_used_at of this APIKey.  # noqa: E501
        :type: int
        """

        self._last_used_at = last_used_at

    @property
    def last_used_ip(self):
        """Gets the last_used_ip of this APIKey.  # noqa: E501


        :return: The last_used_ip of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._last_used_ip

    @last_used_ip.setter
    def last_used_ip(self, last_used_ip):
        """Sets the last_used_ip of this APIKey.


        :param last_used_ip: The last_used_ip of this APIKey.  # noqa: E501
        :type: str
        """

        self._last_used_ip = last_used_ip

    @property
    def last_used_ua(self):
        """Gets the last_used_ua of this APIKey.  # noqa: E501


        :return: The last_used_ua of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._last_used_ua

    @last_used_ua.setter
    def last_used_ua(self, last_used_ua):
        """Sets the last_used_ua of this APIKey.


        :param last_used_ua: The last_used_ua of this APIKey.  # noqa: E501
        :type: str
        """

        self._last_used_ua = last_used_ua

    @property
    def counter(self):
        """Gets the counter of this APIKey.  # noqa: E501


        :return: The counter of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this APIKey.


        :param counter: The counter of this APIKey.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def usage_today(self):
        """Gets the usage_today of this APIKey.  # noqa: E501


        :return: The usage_today of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._usage_today

    @usage_today.setter
    def usage_today(self, usage_today):
        """Sets the usage_today of this APIKey.


        :param usage_today: The usage_today of this APIKey.  # noqa: E501
        :type: int
        """

        self._usage_today = usage_today

    @property
    def usage_limit(self):
        """Gets the usage_limit of this APIKey.  # noqa: E501


        :return: The usage_limit of this APIKey.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this APIKey.


        :param usage_limit: The usage_limit of this APIKey.  # noqa: E501
        :type: int
        """

        self._usage_limit = usage_limit

    @property
    def token(self):
        """Gets the token of this APIKey.  # noqa: E501


        :return: The token of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this APIKey.


        :param token: The token of this APIKey.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def inactive(self):
        """Gets the inactive of this APIKey.  # noqa: E501


        :return: The inactive of this APIKey.  # noqa: E501
        :rtype: bool
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive):
        """Sets the inactive of this APIKey.


        :param inactive: The inactive of this APIKey.  # noqa: E501
        :type: bool
        """

        self._inactive = inactive

    @property
    def type(self):
        """Gets the type of this APIKey.  # noqa: E501


        :return: The type of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this APIKey.


        :param type: The type of this APIKey.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(APIKey, dict):
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
        if not isinstance(other, APIKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
