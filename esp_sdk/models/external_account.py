# coding: utf-8

"""
    ESP Documentation

    This is a description

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExternalAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, created_at=None, updated_at=None, arn=None, account=None, external_id=None, cloudtrail_name=None):
        """
        ExternalAccount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'arn': 'str',
            'account': 'str',
            'external_id': 'str',
            'cloudtrail_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'arn': 'arn',
            'account': 'account',
            'external_id': 'external_id',
            'cloudtrail_name': 'cloudtrail_name'
        }

        self._id = id
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at
        self._arn = arn
        self._account = account
        self._external_id = external_id
        self._cloudtrail_name = cloudtrail_name

    @property
    def id(self):
        """
        Gets the id of this ExternalAccount.
        External Account Id

        :return: The id of this ExternalAccount.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalAccount.
        External Account Id

        :param id: The id of this ExternalAccount.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ExternalAccount.
        Name

        :return: The name of this ExternalAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalAccount.
        Name

        :param name: The name of this ExternalAccount.
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this ExternalAccount.
        Created At

        :return: The created_at of this ExternalAccount.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ExternalAccount.
        Created At

        :param created_at: The created_at of this ExternalAccount.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ExternalAccount.
        Updated At

        :return: The updated_at of this ExternalAccount.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ExternalAccount.
        Updated At

        :param updated_at: The updated_at of this ExternalAccount.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def arn(self):
        """
        Gets the arn of this ExternalAccount.

        :return: The arn of this ExternalAccount.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """
        Sets the arn of this ExternalAccount.

        :param arn: The arn of this ExternalAccount.
        :type: str
        """

        self._arn = arn

    @property
    def account(self):
        """
        Gets the account of this ExternalAccount.

        :return: The account of this ExternalAccount.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this ExternalAccount.

        :param account: The account of this ExternalAccount.
        :type: str
        """

        self._account = account

    @property
    def external_id(self):
        """
        Gets the external_id of this ExternalAccount.

        :return: The external_id of this ExternalAccount.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this ExternalAccount.

        :param external_id: The external_id of this ExternalAccount.
        :type: str
        """

        self._external_id = external_id

    @property
    def cloudtrail_name(self):
        """
        Gets the cloudtrail_name of this ExternalAccount.

        :return: The cloudtrail_name of this ExternalAccount.
        :rtype: str
        """
        return self._cloudtrail_name

    @cloudtrail_name.setter
    def cloudtrail_name(self, cloudtrail_name):
        """
        Sets the cloudtrail_name of this ExternalAccount.

        :param cloudtrail_name: The cloudtrail_name of this ExternalAccount.
        :type: str
        """

        self._cloudtrail_name = cloudtrail_name

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
        if not isinstance(other, ExternalAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other