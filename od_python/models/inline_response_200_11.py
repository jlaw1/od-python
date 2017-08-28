# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 17.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20011(object):
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
        'my_word_counts': 'object',
        'all_word_counts': 'object'
    }

    attribute_map = {
        'my_word_counts': 'my_word_counts',
        'all_word_counts': 'all_word_counts'
    }

    def __init__(self, my_word_counts=None, all_word_counts=None):
        """
        InlineResponse20011 - a model defined in Swagger
        """

        self._my_word_counts = None
        self._all_word_counts = None

        if my_word_counts is not None:
          self.my_word_counts = my_word_counts
        if all_word_counts is not None:
          self.all_word_counts = all_word_counts

    @property
    def my_word_counts(self):
        """
        Gets the my_word_counts of this InlineResponse20011.
        my_word_counts

        :return: The my_word_counts of this InlineResponse20011.
        :rtype: object
        """
        return self._my_word_counts

    @my_word_counts.setter
    def my_word_counts(self, my_word_counts):
        """
        Sets the my_word_counts of this InlineResponse20011.
        my_word_counts

        :param my_word_counts: The my_word_counts of this InlineResponse20011.
        :type: object
        """

        self._my_word_counts = my_word_counts

    @property
    def all_word_counts(self):
        """
        Gets the all_word_counts of this InlineResponse20011.
        all_word_counts

        :return: The all_word_counts of this InlineResponse20011.
        :rtype: object
        """
        return self._all_word_counts

    @all_word_counts.setter
    def all_word_counts(self, all_word_counts):
        """
        Sets the all_word_counts of this InlineResponse20011.
        all_word_counts

        :param all_word_counts: The all_word_counts of this InlineResponse20011.
        :type: object
        """

        self._all_word_counts = all_word_counts

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
        if not isinstance(other, InlineResponse20011):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
