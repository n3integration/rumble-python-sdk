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

class APIKeyOptions(object):
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
        'comment': 'str',
        'organization_id': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'organization_id': 'organization_id'
    }

    def __init__(self, comment:str=None, organization_id:str=None):  # noqa: E501
        """APIKeyOptions - a model defined in Swagger"""  # noqa: E501
        self._comment = None
        self._organization_id = None
        self.discriminator = None
        if comment is not None:
            self.comment = comment
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def comment(self):
        """Gets the comment of this APIKeyOptions.  # noqa: E501


        :return: The comment of this APIKeyOptions.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this APIKeyOptions.


        :param comment: The comment of this APIKeyOptions.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def organization_id(self):
        """Gets the organization_id of this APIKeyOptions.  # noqa: E501


        :return: The organization_id of this APIKeyOptions.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this APIKeyOptions.


        :param organization_id: The organization_id of this APIKeyOptions.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

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
        if issubclass(APIKeyOptions, dict):
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
        if not isinstance(other, APIKeyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
