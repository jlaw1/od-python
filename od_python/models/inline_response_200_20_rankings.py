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


class InlineResponse20020Rankings(object):
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
        'score': 'str',
        'steamid': 'str',
        'avatar': 'str',
        'avatarmedium': 'str',
        'avatarfull': 'str',
        'profileurl': 'str',
        'personaname': 'str',
        'cheese': 'float',
        'fh_unavailable': 'bool',
        'loccountrycode': 'str',
        'solo_competitive_rank': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'score': 'score',
        'steamid': 'steamid',
        'avatar': 'avatar',
        'avatarmedium': 'avatarmedium',
        'avatarfull': 'avatarfull',
        'profileurl': 'profileurl',
        'personaname': 'personaname',
        'cheese': 'cheese',
        'fh_unavailable': 'fh_unavailable',
        'loccountrycode': 'loccountrycode',
        'solo_competitive_rank': 'solo_competitive_rank'
    }

    def __init__(self, account_id=None, score=None, steamid=None, avatar=None, avatarmedium=None, avatarfull=None, profileurl=None, personaname=None, cheese=None, fh_unavailable=None, loccountrycode=None, solo_competitive_rank=None):
        """
        InlineResponse20020Rankings - a model defined in Swagger
        """

        self._account_id = None
        self._score = None
        self._steamid = None
        self._avatar = None
        self._avatarmedium = None
        self._avatarfull = None
        self._profileurl = None
        self._personaname = None
        self._cheese = None
        self._fh_unavailable = None
        self._loccountrycode = None
        self._solo_competitive_rank = None

        if account_id is not None:
          self.account_id = account_id
        if score is not None:
          self.score = score
        if steamid is not None:
          self.steamid = steamid
        if avatar is not None:
          self.avatar = avatar
        if avatarmedium is not None:
          self.avatarmedium = avatarmedium
        if avatarfull is not None:
          self.avatarfull = avatarfull
        if profileurl is not None:
          self.profileurl = profileurl
        if personaname is not None:
          self.personaname = personaname
        if cheese is not None:
          self.cheese = cheese
        if fh_unavailable is not None:
          self.fh_unavailable = fh_unavailable
        if loccountrycode is not None:
          self.loccountrycode = loccountrycode
        if solo_competitive_rank is not None:
          self.solo_competitive_rank = solo_competitive_rank

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse20020Rankings.
        account_id

        :return: The account_id of this InlineResponse20020Rankings.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse20020Rankings.
        account_id

        :param account_id: The account_id of this InlineResponse20020Rankings.
        :type: int
        """

        self._account_id = account_id

    @property
    def score(self):
        """
        Gets the score of this InlineResponse20020Rankings.
        score

        :return: The score of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this InlineResponse20020Rankings.
        score

        :param score: The score of this InlineResponse20020Rankings.
        :type: str
        """

        self._score = score

    @property
    def steamid(self):
        """
        Gets the steamid of this InlineResponse20020Rankings.
        steamid

        :return: The steamid of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._steamid

    @steamid.setter
    def steamid(self, steamid):
        """
        Sets the steamid of this InlineResponse20020Rankings.
        steamid

        :param steamid: The steamid of this InlineResponse20020Rankings.
        :type: str
        """

        self._steamid = steamid

    @property
    def avatar(self):
        """
        Gets the avatar of this InlineResponse20020Rankings.
        avatar

        :return: The avatar of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this InlineResponse20020Rankings.
        avatar

        :param avatar: The avatar of this InlineResponse20020Rankings.
        :type: str
        """

        self._avatar = avatar

    @property
    def avatarmedium(self):
        """
        Gets the avatarmedium of this InlineResponse20020Rankings.
        avatarmedium

        :return: The avatarmedium of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._avatarmedium

    @avatarmedium.setter
    def avatarmedium(self, avatarmedium):
        """
        Sets the avatarmedium of this InlineResponse20020Rankings.
        avatarmedium

        :param avatarmedium: The avatarmedium of this InlineResponse20020Rankings.
        :type: str
        """

        self._avatarmedium = avatarmedium

    @property
    def avatarfull(self):
        """
        Gets the avatarfull of this InlineResponse20020Rankings.
        avatarfull

        :return: The avatarfull of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._avatarfull

    @avatarfull.setter
    def avatarfull(self, avatarfull):
        """
        Sets the avatarfull of this InlineResponse20020Rankings.
        avatarfull

        :param avatarfull: The avatarfull of this InlineResponse20020Rankings.
        :type: str
        """

        self._avatarfull = avatarfull

    @property
    def profileurl(self):
        """
        Gets the profileurl of this InlineResponse20020Rankings.
        profileurl

        :return: The profileurl of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._profileurl

    @profileurl.setter
    def profileurl(self, profileurl):
        """
        Sets the profileurl of this InlineResponse20020Rankings.
        profileurl

        :param profileurl: The profileurl of this InlineResponse20020Rankings.
        :type: str
        """

        self._profileurl = profileurl

    @property
    def personaname(self):
        """
        Gets the personaname of this InlineResponse20020Rankings.
        personaname

        :return: The personaname of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._personaname

    @personaname.setter
    def personaname(self, personaname):
        """
        Sets the personaname of this InlineResponse20020Rankings.
        personaname

        :param personaname: The personaname of this InlineResponse20020Rankings.
        :type: str
        """

        self._personaname = personaname

    @property
    def cheese(self):
        """
        Gets the cheese of this InlineResponse20020Rankings.
        cheese

        :return: The cheese of this InlineResponse20020Rankings.
        :rtype: float
        """
        return self._cheese

    @cheese.setter
    def cheese(self, cheese):
        """
        Sets the cheese of this InlineResponse20020Rankings.
        cheese

        :param cheese: The cheese of this InlineResponse20020Rankings.
        :type: float
        """

        self._cheese = cheese

    @property
    def fh_unavailable(self):
        """
        Gets the fh_unavailable of this InlineResponse20020Rankings.
        fh_unavailable

        :return: The fh_unavailable of this InlineResponse20020Rankings.
        :rtype: bool
        """
        return self._fh_unavailable

    @fh_unavailable.setter
    def fh_unavailable(self, fh_unavailable):
        """
        Sets the fh_unavailable of this InlineResponse20020Rankings.
        fh_unavailable

        :param fh_unavailable: The fh_unavailable of this InlineResponse20020Rankings.
        :type: bool
        """

        self._fh_unavailable = fh_unavailable

    @property
    def loccountrycode(self):
        """
        Gets the loccountrycode of this InlineResponse20020Rankings.
        loccountrycode

        :return: The loccountrycode of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._loccountrycode

    @loccountrycode.setter
    def loccountrycode(self, loccountrycode):
        """
        Sets the loccountrycode of this InlineResponse20020Rankings.
        loccountrycode

        :param loccountrycode: The loccountrycode of this InlineResponse20020Rankings.
        :type: str
        """

        self._loccountrycode = loccountrycode

    @property
    def solo_competitive_rank(self):
        """
        Gets the solo_competitive_rank of this InlineResponse20020Rankings.
        solo_competitive_rank

        :return: The solo_competitive_rank of this InlineResponse20020Rankings.
        :rtype: str
        """
        return self._solo_competitive_rank

    @solo_competitive_rank.setter
    def solo_competitive_rank(self, solo_competitive_rank):
        """
        Sets the solo_competitive_rank of this InlineResponse20020Rankings.
        solo_competitive_rank

        :param solo_competitive_rank: The solo_competitive_rank of this InlineResponse20020Rankings.
        :type: str
        """

        self._solo_competitive_rank = solo_competitive_rank

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
        if not isinstance(other, InlineResponse20020Rankings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
