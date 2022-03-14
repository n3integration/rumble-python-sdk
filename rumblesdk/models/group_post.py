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

class GroupPost(object):
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
        'description': 'str',
        'name': 'str',
        'expires_at': 'int',
        'org_default_role': 'str',
        'org_roles': 'dict(str, object)'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'expires_at': 'expires_at',
        'org_default_role': 'org_default_role',
        'org_roles': 'org_roles'
    }

    def __init__(self, description:str=None, name:str=None, expires_at:int=None, org_default_role:str=None, org_roles:dict=None):  # noqa: E501
        """GroupPost - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._expires_at = None
        self._org_default_role = None
        self._org_roles = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if expires_at is not None:
            self.expires_at = expires_at
        if org_default_role is not None:
            self.org_default_role = org_default_role
        if org_roles is not None:
            self.org_roles = org_roles

    @property
    def description(self):
        """Gets the description of this GroupPost.  # noqa: E501


        :return: The description of this GroupPost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupPost.


        :param description: The description of this GroupPost.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this GroupPost.  # noqa: E501


        :return: The name of this GroupPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupPost.


        :param name: The name of this GroupPost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def expires_at(self):
        """Gets the expires_at of this GroupPost.  # noqa: E501


        :return: The expires_at of this GroupPost.  # noqa: E501
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this GroupPost.


        :param expires_at: The expires_at of this GroupPost.  # noqa: E501
        :type: int
        """

        self._expires_at = expires_at

    @property
    def org_default_role(self):
        """Gets the org_default_role of this GroupPost.  # noqa: E501


        :return: The org_default_role of this GroupPost.  # noqa: E501
        :rtype: str
        """
        return self._org_default_role

    @org_default_role.setter
    def org_default_role(self, org_default_role):
        """Sets the org_default_role of this GroupPost.


        :param org_default_role: The org_default_role of this GroupPost.  # noqa: E501
        :type: str
        """

        self._org_default_role = org_default_role

    @property
    def org_roles(self):
        """Gets the org_roles of this GroupPost.  # noqa: E501


        :return: The org_roles of this GroupPost.  # noqa: E501
        :rtype: dict
        """
        return self._org_roles

    @org_roles.setter
    def org_roles(self, org_roles):
        """Sets the org_roles of this GroupPost.


        :param org_roles: The org_roles of this GroupPost.  # noqa: E501
        :type: dict
        """

        self._org_roles = org_roles

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
        if issubclass(GroupPost, dict):
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
        if not isinstance(other, GroupPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
