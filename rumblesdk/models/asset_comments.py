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

class AssetComments(object):
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
        'comments': 'str'
    }

    attribute_map = {
        'comments': 'comments'
    }

    def __init__(self, comments:str=None):  # noqa: E501
        """AssetComments - a model defined in Swagger"""  # noqa: E501
        self._comments = None
        self.discriminator = None
        self.comments = comments

    @property
    def comments(self):
        """Gets the comments of this AssetComments.  # noqa: E501


        :return: The comments of this AssetComments.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AssetComments.


        :param comments: The comments of this AssetComments.  # noqa: E501
        :type: str
        """
        if comments is None:
            raise ValueError("Invalid value for `comments`, must not be `None`")  # noqa: E501

        self._comments = comments

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
        if issubclass(AssetComments, dict):
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
        if not isinstance(other, AssetComments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other