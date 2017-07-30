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


class InlineResponse200Chat(object):
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
        'time': 'int',
        'unit': 'str',
        'key': 'str',
        'slot': 'int',
        'player_slot': 'int'
    }

    attribute_map = {
        'time': 'time',
        'unit': 'unit',
        'key': 'key',
        'slot': 'slot',
        'player_slot': 'player_slot'
    }

    def __init__(self, time=None, unit=None, key=None, slot=None, player_slot=None):
        """
        InlineResponse200Chat - a model defined in Swagger
        """

        self._time = None
        self._unit = None
        self._key = None
        self._slot = None
        self._player_slot = None

        if time is not None:
          self.time = time
        if unit is not None:
          self.unit = unit
        if key is not None:
          self.key = key
        if slot is not None:
          self.slot = slot
        if player_slot is not None:
          self.player_slot = player_slot

    @property
    def time(self):
        """
        Gets the time of this InlineResponse200Chat.
        time

        :return: The time of this InlineResponse200Chat.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this InlineResponse200Chat.
        time

        :param time: The time of this InlineResponse200Chat.
        :type: int
        """

        self._time = time

    @property
    def unit(self):
        """
        Gets the unit of this InlineResponse200Chat.
        player name

        :return: The unit of this InlineResponse200Chat.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this InlineResponse200Chat.
        player name

        :param unit: The unit of this InlineResponse200Chat.
        :type: str
        """

        self._unit = unit

    @property
    def key(self):
        """
        Gets the key of this InlineResponse200Chat.
        words

        :return: The key of this InlineResponse200Chat.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this InlineResponse200Chat.
        words

        :param key: The key of this InlineResponse200Chat.
        :type: str
        """

        self._key = key

    @property
    def slot(self):
        """
        Gets the slot of this InlineResponse200Chat.
        slot

        :return: The slot of this InlineResponse200Chat.
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """
        Sets the slot of this InlineResponse200Chat.
        slot

        :param slot: The slot of this InlineResponse200Chat.
        :type: int
        """

        self._slot = slot

    @property
    def player_slot(self):
        """
        Gets the player_slot of this InlineResponse200Chat.
        player_slot

        :return: The player_slot of this InlineResponse200Chat.
        :rtype: int
        """
        return self._player_slot

    @player_slot.setter
    def player_slot(self, player_slot):
        """
        Sets the player_slot of this InlineResponse200Chat.
        player_slot

        :param player_slot: The player_slot of this InlineResponse200Chat.
        :type: int
        """

        self._player_slot = player_slot

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
        if not isinstance(other, InlineResponse200Chat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
