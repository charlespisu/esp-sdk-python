# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class Signature(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, relationships=None, errors=None, id=None, created_at=None, description=None, identifier=None, name=None, resolution=None, risk_level=None, updated_at=None, service=None, service_id=None):
        """
        Signature - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'relationships': 'object',
            'errors': 'list[str]',
            'id': 'int',
            'created_at': 'datetime',
            'description': 'str',
            'identifier': 'str',
            'name': 'str',
            'resolution': 'str',
            'risk_level': 'str',
            'updated_at': 'datetime',
            'service': 'Service',
            'service_id': 'int'
        }

        self.attribute_map = {
            'relationships': 'relationships',
            'errors': 'errors',
            'id': 'id',
            'created_at': 'created_at',
            'description': 'description',
            'identifier': 'identifier',
            'name': 'name',
            'resolution': 'resolution',
            'risk_level': 'risk_level',
            'updated_at': 'updated_at',
            'service': 'service',
            'service_id': 'service_id'
        }

        self._relationships = relationships
        self._errors = errors
        self._id = id
        self._created_at = created_at
        self._description = description
        self._identifier = identifier
        self._name = name
        self._resolution = resolution
        self._risk_level = risk_level
        self._updated_at = updated_at
        self._service = service
        self._service_id = service_id

    @property
    def relationships(self):
        """
        Gets the relationships of this Signature.
        Links to Associated Objects

        :return: The relationships of this Signature.
        :rtype: object
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Signature.
        Links to Associated Objects

        :param relationships: The relationships of this Signature.
        :type: object
        """

        self._relationships = relationships

    @property
    def errors(self):
        """
        Gets the errors of this Signature.
        Array of error messages if the request failed

        :return: The errors of this Signature.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this Signature.
        Array of error messages if the request failed

        :param errors: The errors of this Signature.
        :type: list[str]
        """

        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this Signature.
        Unique Id

        :return: The id of this Signature.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Signature.
        Unique Id

        :param id: The id of this Signature.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Signature.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Signature.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Signature.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Signature.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """
        Gets the description of this Signature.
        The description of the signature

        :return: The description of this Signature.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Signature.
        The description of the signature

        :param description: The description of this Signature.
        :type: str
        """

        self._description = description

    @property
    def identifier(self):
        """
        Gets the identifier of this Signature.
        The identifier of the signature

        :return: The identifier of this Signature.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Signature.
        The identifier of the signature

        :param identifier: The identifier of this Signature.
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this Signature.
        The name of the signature

        :return: The name of this Signature.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Signature.
        The name of the signature

        :param name: The name of this Signature.
        :type: str
        """

        self._name = name

    @property
    def resolution(self):
        """
        Gets the resolution of this Signature.
        Details for how to resolve this signature

        :return: The resolution of this Signature.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this Signature.
        Details for how to resolve this signature

        :param resolution: The resolution of this Signature.
        :type: str
        """

        self._resolution = resolution

    @property
    def risk_level(self):
        """
        Gets the risk_level of this Signature.
        The risk-level of the problem identified by the signature. Valid values are Low, Medium, High

        :return: The risk_level of this Signature.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this Signature.
        The risk-level of the problem identified by the signature. Valid values are Low, Medium, High

        :param risk_level: The risk_level of this Signature.
        :type: str
        """

        self._risk_level = risk_level

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Signature.
        ISO 8601 timestamp when the resource was last updated

        :return: The updated_at of this Signature.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Signature.
        ISO 8601 timestamp when the resource was last updated

        :param updated_at: The updated_at of this Signature.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def service(self):
        """
        Gets the service of this Signature.
        Associated Service

        :return: The service of this Signature.
        :rtype: Service
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this Signature.
        Associated Service

        :param service: The service of this Signature.
        :type: Service
        """

        self._service = service

    @property
    def service_id(self):
        """
        Gets the service_id of this Signature.
        Associated Service Id

        :return: The service_id of this Signature.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """
        Sets the service_id of this Signature.
        Associated Service Id

        :param service_id: The service_id of this Signature.
        :type: int
        """

        self._service_id = service_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
