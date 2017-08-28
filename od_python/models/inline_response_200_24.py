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


class InlineResponse20024(object):
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
        'team_id': 'int',
        'rating': 'float',
        'wins': 'int',
        'losses': 'int',
        'last_match_time': 'int',
        'name': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'team_id': 'team_id',
        'rating': 'rating',
        'wins': 'wins',
        'losses': 'losses',
        'last_match_time': 'last_match_time',
        'name': 'name',
        'tag': 'tag'
    }

    def __init__(self, team_id=None, rating=None, wins=None, losses=None, last_match_time=None, name=None, tag=None):
        """
        InlineResponse20024 - a model defined in Swagger
        """

        self._team_id = None
        self._rating = None
        self._wins = None
        self._losses = None
        self._last_match_time = None
        self._name = None
        self._tag = None

        if team_id is not None:
          self.team_id = team_id
        if rating is not None:
          self.rating = rating
        if wins is not None:
          self.wins = wins
        if losses is not None:
          self.losses = losses
        if last_match_time is not None:
          self.last_match_time = last_match_time
        if name is not None:
          self.name = name
        if tag is not None:
          self.tag = tag

    @property
    def team_id(self):
        """
        Gets the team_id of this InlineResponse20024.
        team_id

        :return: The team_id of this InlineResponse20024.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this InlineResponse20024.
        team_id

        :param team_id: The team_id of this InlineResponse20024.
        :type: int
        """

        self._team_id = team_id

    @property
    def rating(self):
        """
        Gets the rating of this InlineResponse20024.
        The Elo rating of the team

        :return: The rating of this InlineResponse20024.
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """
        Sets the rating of this InlineResponse20024.
        The Elo rating of the team

        :param rating: The rating of this InlineResponse20024.
        :type: float
        """

        self._rating = rating

    @property
    def wins(self):
        """
        Gets the wins of this InlineResponse20024.
        The number of games won by this team

        :return: The wins of this InlineResponse20024.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """
        Sets the wins of this InlineResponse20024.
        The number of games won by this team

        :param wins: The wins of this InlineResponse20024.
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """
        Gets the losses of this InlineResponse20024.
        The number of losses by this team

        :return: The losses of this InlineResponse20024.
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """
        Sets the losses of this InlineResponse20024.
        The number of losses by this team

        :param losses: The losses of this InlineResponse20024.
        :type: int
        """

        self._losses = losses

    @property
    def last_match_time(self):
        """
        Gets the last_match_time of this InlineResponse20024.
        The Unix timestamp of the last match played by this team

        :return: The last_match_time of this InlineResponse20024.
        :rtype: int
        """
        return self._last_match_time

    @last_match_time.setter
    def last_match_time(self, last_match_time):
        """
        Sets the last_match_time of this InlineResponse20024.
        The Unix timestamp of the last match played by this team

        :param last_match_time: The last_match_time of this InlineResponse20024.
        :type: int
        """

        self._last_match_time = last_match_time

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20024.
        name

        :return: The name of this InlineResponse20024.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20024.
        name

        :param name: The name of this InlineResponse20024.
        :type: str
        """

        self._name = name

    @property
    def tag(self):
        """
        Gets the tag of this InlineResponse20024.
        The team tag

        :return: The tag of this InlineResponse20024.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this InlineResponse20024.
        The team tag

        :param tag: The tag of this InlineResponse20024.
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, InlineResponse20024):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
