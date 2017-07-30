# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 16.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20021ResultGoldPerMin(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'percentile': 'float',
        'value': 'float'
    }

    attribute_map = {
        'percentile': 'percentile',
        'value': 'value'
    }

    def __init__(self, percentile=None, value=None):
        """
        InlineResponse20021ResultGoldPerMin - a model defined in Swagger
        """

        self._percentile = None
        self._value = None

        if percentile is not None:
          self.percentile = percentile
        if value is not None:
          self.value = value

    @property
    def percentile(self):
        """
        Gets the percentile of this InlineResponse20021ResultGoldPerMin.
        percentile

        :return: The percentile of this InlineResponse20021ResultGoldPerMin.
        :rtype: float
        """
        return self._percentile

    @percentile.setter
    def percentile(self, percentile):
        """
        Sets the percentile of this InlineResponse20021ResultGoldPerMin.
        percentile

        :param percentile: The percentile of this InlineResponse20021ResultGoldPerMin.
        :type: float
        """

        self._percentile = percentile

    @property
    def value(self):
        """
        Gets the value of this InlineResponse20021ResultGoldPerMin.
        value

        :return: The value of this InlineResponse20021ResultGoldPerMin.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this InlineResponse20021ResultGoldPerMin.
        value

        :param value: The value of this InlineResponse20021ResultGoldPerMin.
        :type: float
        """

        self._value = value

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
        if not isinstance(other, InlineResponse20021ResultGoldPerMin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
