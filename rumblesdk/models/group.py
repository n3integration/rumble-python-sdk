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

class Group(object):
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
        'description': 'str',
        'name': 'str',
        'role_summary': 'str',
        'user_count': 'int',
        'created_by_email': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'expires_at': 'int',
        'org_default_role': 'str',
        'org_roles': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'role_summary': 'role_summary',
        'user_count': 'user_count',
        'created_by_email': 'created_by_email',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'expires_at': 'expires_at',
        'org_default_role': 'org_default_role',
        'org_roles': 'org_roles'
    }

    def __init__(self, id:str=None, description:str=None, name:str=None, role_summary:str=None, user_count:int=None, created_by_email:str=None, created_at:int=None, updated_at:int=None, expires_at:int=None, org_default_role:str=None, org_roles:dict=None):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._name = None
        self._role_summary = None
        self._user_count = None
        self._created_by_email = None
        self._created_at = None
        self._updated_at = None
        self._expires_at = None
        self._org_default_role = None
        self._org_roles = None
        self.discriminator = None
        self.id = id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if role_summary is not None:
            self.role_summary = role_summary
        if user_count is not None:
            self.user_count = user_count
        if created_by_email is not None:
            self.created_by_email = created_by_email
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if expires_at is not None:
            self.expires_at = expires_at
        if org_default_role is not None:
            self.org_default_role = org_default_role
        if org_roles is not None:
            self.org_roles = org_roles

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this Group.  # noqa: E501


        :return: The description of this Group.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Group.


        :param description: The description of this Group.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501


        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.


        :param name: The name of this Group.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role_summary(self):
        """Gets the role_summary of this Group.  # noqa: E501


        :return: The role_summary of this Group.  # noqa: E501
        :rtype: str
        """
        return self._role_summary

    @role_summary.setter
    def role_summary(self, role_summary):
        """Sets the role_summary of this Group.


        :param role_summary: The role_summary of this Group.  # noqa: E501
        :type: str
        """

        self._role_summary = role_summary

    @property
    def user_count(self):
        """Gets the user_count of this Group.  # noqa: E501


        :return: The user_count of this Group.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this Group.


        :param user_count: The user_count of this Group.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def created_by_email(self):
        """Gets the created_by_email of this Group.  # noqa: E501


        :return: The created_by_email of this Group.  # noqa: E501
        :rtype: str
        """
        return self._created_by_email

    @created_by_email.setter
    def created_by_email(self, created_by_email):
        """Sets the created_by_email of this Group.


        :param created_by_email: The created_by_email of this Group.  # noqa: E501
        :type: str
        """

        self._created_by_email = created_by_email

    @property
    def created_at(self):
        """Gets the created_at of this Group.  # noqa: E501


        :return: The created_at of this Group.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Group.


        :param created_at: The created_at of this Group.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Group.  # noqa: E501


        :return: The updated_at of this Group.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Group.


        :param updated_at: The updated_at of this Group.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def expires_at(self):
        """Gets the expires_at of this Group.  # noqa: E501


        :return: The expires_at of this Group.  # noqa: E501
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Group.


        :param expires_at: The expires_at of this Group.  # noqa: E501
        :type: int
        """

        self._expires_at = expires_at

    @property
    def org_default_role(self):
        """Gets the org_default_role of this Group.  # noqa: E501


        :return: The org_default_role of this Group.  # noqa: E501
        :rtype: str
        """
        return self._org_default_role

    @org_default_role.setter
    def org_default_role(self, org_default_role):
        """Sets the org_default_role of this Group.


        :param org_default_role: The org_default_role of this Group.  # noqa: E501
        :type: str
        """

        self._org_default_role = org_default_role

    @property
    def org_roles(self):
        """Gets the org_roles of this Group.  # noqa: E501


        :return: The org_roles of this Group.  # noqa: E501
        :rtype: dict
        """
        return self._org_roles

    @org_roles.setter
    def org_roles(self, org_roles):
        """Sets the org_roles of this Group.


        :param org_roles: The org_roles of this Group.  # noqa: E501
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
        if issubclass(Group, dict):
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
