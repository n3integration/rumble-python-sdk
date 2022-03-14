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

class SiteOptions(object):
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
        'name': 'str',
        'description': 'str',
        'scope': 'str',
        'excludes': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'scope': 'scope',
        'excludes': 'excludes'
    }

    def __init__(self, name:str=None, description:str=None, scope:str=None, excludes:str=None):  # noqa: E501
        """SiteOptions - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._scope = None
        self._excludes = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        if scope is not None:
            self.scope = scope
        if excludes is not None:
            self.excludes = excludes

    @property
    def name(self):
        """Gets the name of this SiteOptions.  # noqa: E501


        :return: The name of this SiteOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteOptions.


        :param name: The name of this SiteOptions.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this SiteOptions.  # noqa: E501


        :return: The description of this SiteOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SiteOptions.


        :param description: The description of this SiteOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def scope(self):
        """Gets the scope of this SiteOptions.  # noqa: E501


        :return: The scope of this SiteOptions.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SiteOptions.


        :param scope: The scope of this SiteOptions.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def excludes(self):
        """Gets the excludes of this SiteOptions.  # noqa: E501


        :return: The excludes of this SiteOptions.  # noqa: E501
        :rtype: str
        """
        return self._excludes

    @excludes.setter
    def excludes(self, excludes):
        """Sets the excludes of this SiteOptions.


        :param excludes: The excludes of this SiteOptions.  # noqa: E501
        :type: str
        """

        self._excludes = excludes

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
        if issubclass(SiteOptions, dict):
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
        if not isinstance(other, SiteOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
