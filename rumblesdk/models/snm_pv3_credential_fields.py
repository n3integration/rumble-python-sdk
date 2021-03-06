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

class SNMPv3CredentialFields(object):
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
        'username': 'str',
        'context': 'str',
        'auth_protocol': 'str',
        'auth_passphrase': 'str',
        'privacy_protocol': 'str',
        'privacy_passphrase': 'str'
    }

    attribute_map = {
        'username': 'username',
        'context': 'context',
        'auth_protocol': 'auth-protocol',
        'auth_passphrase': 'auth-passphrase',
        'privacy_protocol': 'privacy-protocol',
        'privacy_passphrase': 'privacy-passphrase'
    }

    def __init__(self, username:str=None, context:str=None, auth_protocol:str=None, auth_passphrase:str=None, privacy_protocol:str=None, privacy_passphrase:str=None):  # noqa: E501
        """SNMPv3CredentialFields - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._context = None
        self._auth_protocol = None
        self._auth_passphrase = None
        self._privacy_protocol = None
        self._privacy_passphrase = None
        self.discriminator = None
        self.username = username
        if context is not None:
            self.context = context
        if auth_protocol is not None:
            self.auth_protocol = auth_protocol
        if auth_passphrase is not None:
            self.auth_passphrase = auth_passphrase
        if privacy_protocol is not None:
            self.privacy_protocol = privacy_protocol
        if privacy_passphrase is not None:
            self.privacy_passphrase = privacy_passphrase

    @property
    def username(self):
        """Gets the username of this SNMPv3CredentialFields.  # noqa: E501


        :return: The username of this SNMPv3CredentialFields.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SNMPv3CredentialFields.


        :param username: The username of this SNMPv3CredentialFields.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def context(self):
        """Gets the context of this SNMPv3CredentialFields.  # noqa: E501


        :return: The context of this SNMPv3CredentialFields.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this SNMPv3CredentialFields.


        :param context: The context of this SNMPv3CredentialFields.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def auth_protocol(self):
        """Gets the auth_protocol of this SNMPv3CredentialFields.  # noqa: E501


        :return: The auth_protocol of this SNMPv3CredentialFields.  # noqa: E501
        :rtype: str
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_protocol):
        """Sets the auth_protocol of this SNMPv3CredentialFields.


        :param auth_protocol: The auth_protocol of this SNMPv3CredentialFields.  # noqa: E501
        :type: str
        """

        self._auth_protocol = auth_protocol

    @property
    def auth_passphrase(self):
        """Gets the auth_passphrase of this SNMPv3CredentialFields.  # noqa: E501


        :return: The auth_passphrase of this SNMPv3CredentialFields.  # noqa: E501
        :rtype: str
        """
        return self._auth_passphrase

    @auth_passphrase.setter
    def auth_passphrase(self, auth_passphrase):
        """Sets the auth_passphrase of this SNMPv3CredentialFields.


        :param auth_passphrase: The auth_passphrase of this SNMPv3CredentialFields.  # noqa: E501
        :type: str
        """

        self._auth_passphrase = auth_passphrase

    @property
    def privacy_protocol(self):
        """Gets the privacy_protocol of this SNMPv3CredentialFields.  # noqa: E501


        :return: The privacy_protocol of this SNMPv3CredentialFields.  # noqa: E501
        :rtype: str
        """
        return self._privacy_protocol

    @privacy_protocol.setter
    def privacy_protocol(self, privacy_protocol):
        """Sets the privacy_protocol of this SNMPv3CredentialFields.


        :param privacy_protocol: The privacy_protocol of this SNMPv3CredentialFields.  # noqa: E501
        :type: str
        """

        self._privacy_protocol = privacy_protocol

    @property
    def privacy_passphrase(self):
        """Gets the privacy_passphrase of this SNMPv3CredentialFields.  # noqa: E501


        :return: The privacy_passphrase of this SNMPv3CredentialFields.  # noqa: E501
        :rtype: str
        """
        return self._privacy_passphrase

    @privacy_passphrase.setter
    def privacy_passphrase(self, privacy_passphrase):
        """Sets the privacy_passphrase of this SNMPv3CredentialFields.


        :param privacy_passphrase: The privacy_passphrase of this SNMPv3CredentialFields.  # noqa: E501
        :type: str
        """

        self._privacy_passphrase = privacy_passphrase

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
        if issubclass(SNMPv3CredentialFields, dict):
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
        if not isinstance(other, SNMPv3CredentialFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
