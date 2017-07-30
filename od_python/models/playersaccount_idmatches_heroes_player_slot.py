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


class PlayersaccountIdmatchesHeroesPlayerSlot(object):
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
        'account_id': 'int',
        'hero_id': 'int',
        'player_slot': 'int'
    }

    attribute_map = {
        'account_id': 'account_id',
        'hero_id': 'hero_id',
        'player_slot': 'player_slot'
    }

    def __init__(self, account_id=None, hero_id=None, player_slot=None):
        """
        PlayersaccountIdmatchesHeroesPlayerSlot - a model defined in Swagger
        """

        self._account_id = None
        self._hero_id = None
        self._player_slot = None

        if account_id is not None:
          self.account_id = account_id
        if hero_id is not None:
          self.hero_id = hero_id
        if player_slot is not None:
          self.player_slot = player_slot

    @property
    def account_id(self):
        """
        Gets the account_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        account_id

        :return: The account_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        account_id

        :param account_id: The account_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        :type: int
        """

        self._account_id = account_id

    @property
    def hero_id(self):
        """
        Gets the hero_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        hero_id

        :return: The hero_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        :rtype: int
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        hero_id

        :param hero_id: The hero_id of this PlayersaccountIdmatchesHeroesPlayerSlot.
        :type: int
        """

        self._hero_id = hero_id

    @property
    def player_slot(self):
        """
        Gets the player_slot of this PlayersaccountIdmatchesHeroesPlayerSlot.
        player_slot

        :return: The player_slot of this PlayersaccountIdmatchesHeroesPlayerSlot.
        :rtype: int
        """
        return self._player_slot

    @player_slot.setter
    def player_slot(self, player_slot):
        """
        Sets the player_slot of this PlayersaccountIdmatchesHeroesPlayerSlot.
        player_slot

        :param player_slot: The player_slot of this PlayersaccountIdmatchesHeroesPlayerSlot.
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
        if not isinstance(other, PlayersaccountIdmatchesHeroesPlayerSlot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
