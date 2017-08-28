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


class InlineResponse20023(object):
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
        'leagueid': 'int',
        'ticket': 'str',
        'banner': 'str',
        'tier': 'str',
        'name': 'str'
    }

    attribute_map = {
        'leagueid': 'leagueid',
        'ticket': 'ticket',
        'banner': 'banner',
        'tier': 'tier',
        'name': 'name'
    }

    def __init__(self, leagueid=None, ticket=None, banner=None, tier=None, name=None):
        """
        InlineResponse20023 - a model defined in Swagger
        """

        self._leagueid = None
        self._ticket = None
        self._banner = None
        self._tier = None
        self._name = None

        if leagueid is not None:
          self.leagueid = leagueid
        if ticket is not None:
          self.ticket = ticket
        if banner is not None:
          self.banner = banner
        if tier is not None:
          self.tier = tier
        if name is not None:
          self.name = name

    @property
    def leagueid(self):
        """
        Gets the leagueid of this InlineResponse20023.
        leagueid

        :return: The leagueid of this InlineResponse20023.
        :rtype: int
        """
        return self._leagueid

    @leagueid.setter
    def leagueid(self, leagueid):
        """
        Sets the leagueid of this InlineResponse20023.
        leagueid

        :param leagueid: The leagueid of this InlineResponse20023.
        :type: int
        """

        self._leagueid = leagueid

    @property
    def ticket(self):
        """
        Gets the ticket of this InlineResponse20023.
        ticket

        :return: The ticket of this InlineResponse20023.
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """
        Sets the ticket of this InlineResponse20023.
        ticket

        :param ticket: The ticket of this InlineResponse20023.
        :type: str
        """

        self._ticket = ticket

    @property
    def banner(self):
        """
        Gets the banner of this InlineResponse20023.
        banner

        :return: The banner of this InlineResponse20023.
        :rtype: str
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """
        Sets the banner of this InlineResponse20023.
        banner

        :param banner: The banner of this InlineResponse20023.
        :type: str
        """

        self._banner = banner

    @property
    def tier(self):
        """
        Gets the tier of this InlineResponse20023.
        tier

        :return: The tier of this InlineResponse20023.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this InlineResponse20023.
        tier

        :param tier: The tier of this InlineResponse20023.
        :type: str
        """

        self._tier = tier

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20023.
        name

        :return: The name of this InlineResponse20023.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20023.
        name

        :param name: The name of this InlineResponse20023.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, InlineResponse20023):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
