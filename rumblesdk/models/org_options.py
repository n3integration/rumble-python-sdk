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

class OrgOptions(object):
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
        'export_token': 'str',
        'project': 'str',
        'parent_id': 'str',
        'expiration_assets_stale': 'float',
        'expiration_assets_offline': 'float',
        'expiration_scans': 'float'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'export_token': 'export_token',
        'project': 'project',
        'parent_id': 'parent_id',
        'expiration_assets_stale': 'expiration_assets_stale',
        'expiration_assets_offline': 'expiration_assets_offline',
        'expiration_scans': 'expiration_scans'
    }

    def __init__(self, name:str=None, description:str=None, export_token:str=None, project:str=None, parent_id:str=None, expiration_assets_stale:float=None, expiration_assets_offline:float=None, expiration_scans:float=None):  # noqa: E501
        """OrgOptions - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._export_token = None
        self._project = None
        self._parent_id = None
        self._expiration_assets_stale = None
        self._expiration_assets_offline = None
        self._expiration_scans = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if export_token is not None:
            self.export_token = export_token
        if project is not None:
            self.project = project
        if parent_id is not None:
            self.parent_id = parent_id
        if expiration_assets_stale is not None:
            self.expiration_assets_stale = expiration_assets_stale
        if expiration_assets_offline is not None:
            self.expiration_assets_offline = expiration_assets_offline
        if expiration_scans is not None:
            self.expiration_scans = expiration_scans

    @property
    def name(self):
        """Gets the name of this OrgOptions.  # noqa: E501


        :return: The name of this OrgOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrgOptions.


        :param name: The name of this OrgOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this OrgOptions.  # noqa: E501


        :return: The description of this OrgOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrgOptions.


        :param description: The description of this OrgOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def export_token(self):
        """Gets the export_token of this OrgOptions.  # noqa: E501


        :return: The export_token of this OrgOptions.  # noqa: E501
        :rtype: str
        """
        return self._export_token

    @export_token.setter
    def export_token(self, export_token):
        """Sets the export_token of this OrgOptions.


        :param export_token: The export_token of this OrgOptions.  # noqa: E501
        :type: str
        """

        self._export_token = export_token

    @property
    def project(self):
        """Gets the project of this OrgOptions.  # noqa: E501


        :return: The project of this OrgOptions.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this OrgOptions.


        :param project: The project of this OrgOptions.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def parent_id(self):
        """Gets the parent_id of this OrgOptions.  # noqa: E501


        :return: The parent_id of this OrgOptions.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this OrgOptions.


        :param parent_id: The parent_id of this OrgOptions.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def expiration_assets_stale(self):
        """Gets the expiration_assets_stale of this OrgOptions.  # noqa: E501


        :return: The expiration_assets_stale of this OrgOptions.  # noqa: E501
        :rtype: float
        """
        return self._expiration_assets_stale

    @expiration_assets_stale.setter
    def expiration_assets_stale(self, expiration_assets_stale):
        """Sets the expiration_assets_stale of this OrgOptions.


        :param expiration_assets_stale: The expiration_assets_stale of this OrgOptions.  # noqa: E501
        :type: float
        """

        self._expiration_assets_stale = expiration_assets_stale

    @property
    def expiration_assets_offline(self):
        """Gets the expiration_assets_offline of this OrgOptions.  # noqa: E501


        :return: The expiration_assets_offline of this OrgOptions.  # noqa: E501
        :rtype: float
        """
        return self._expiration_assets_offline

    @expiration_assets_offline.setter
    def expiration_assets_offline(self, expiration_assets_offline):
        """Sets the expiration_assets_offline of this OrgOptions.


        :param expiration_assets_offline: The expiration_assets_offline of this OrgOptions.  # noqa: E501
        :type: float
        """

        self._expiration_assets_offline = expiration_assets_offline

    @property
    def expiration_scans(self):
        """Gets the expiration_scans of this OrgOptions.  # noqa: E501


        :return: The expiration_scans of this OrgOptions.  # noqa: E501
        :rtype: float
        """
        return self._expiration_scans

    @expiration_scans.setter
    def expiration_scans(self, expiration_scans):
        """Sets the expiration_scans of this OrgOptions.


        :param expiration_scans: The expiration_scans of this OrgOptions.  # noqa: E501
        :type: float
        """

        self._expiration_scans = expiration_scans

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
        if issubclass(OrgOptions, dict):
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
        if not isinstance(other, OrgOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
