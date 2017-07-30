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


class InlineResponse2001Profile(object):
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
        'personaname': 'str',
        'name': 'str',
        'cheese': 'float',
        'steamid': 'str',
        'avatar': 'str',
        'avatarmedium': 'str',
        'avatarfull': 'str',
        'profileurl': 'str',
        'last_login': 'str',
        'loccountrycode': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'personaname': 'personaname',
        'name': 'name',
        'cheese': 'cheese',
        'steamid': 'steamid',
        'avatar': 'avatar',
        'avatarmedium': 'avatarmedium',
        'avatarfull': 'avatarfull',
        'profileurl': 'profileurl',
        'last_login': 'last_login',
        'loccountrycode': 'loccountrycode'
    }

    def __init__(self, account_id=None, personaname=None, name=None, cheese=None, steamid=None, avatar=None, avatarmedium=None, avatarfull=None, profileurl=None, last_login=None, loccountrycode=None):
        """
        InlineResponse2001Profile - a model defined in Swagger
        """

        self._account_id = None
        self._personaname = None
        self._name = None
        self._cheese = None
        self._steamid = None
        self._avatar = None
        self._avatarmedium = None
        self._avatarfull = None
        self._profileurl = None
        self._last_login = None
        self._loccountrycode = None

        if account_id is not None:
          self.account_id = account_id
        if personaname is not None:
          self.personaname = personaname
        if name is not None:
          self.name = name
        if cheese is not None:
          self.cheese = cheese
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
        if last_login is not None:
          self.last_login = last_login
        if loccountrycode is not None:
          self.loccountrycode = loccountrycode

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse2001Profile.
        account_id

        :return: The account_id of this InlineResponse2001Profile.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse2001Profile.
        account_id

        :param account_id: The account_id of this InlineResponse2001Profile.
        :type: int
        """

        self._account_id = account_id

    @property
    def personaname(self):
        """
        Gets the personaname of this InlineResponse2001Profile.
        personaname

        :return: The personaname of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._personaname

    @personaname.setter
    def personaname(self, personaname):
        """
        Sets the personaname of this InlineResponse2001Profile.
        personaname

        :param personaname: The personaname of this InlineResponse2001Profile.
        :type: str
        """

        self._personaname = personaname

    @property
    def name(self):
        """
        Gets the name of this InlineResponse2001Profile.
        name

        :return: The name of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse2001Profile.
        name

        :param name: The name of this InlineResponse2001Profile.
        :type: str
        """

        self._name = name

    @property
    def cheese(self):
        """
        Gets the cheese of this InlineResponse2001Profile.
        cheese

        :return: The cheese of this InlineResponse2001Profile.
        :rtype: float
        """
        return self._cheese

    @cheese.setter
    def cheese(self, cheese):
        """
        Sets the cheese of this InlineResponse2001Profile.
        cheese

        :param cheese: The cheese of this InlineResponse2001Profile.
        :type: float
        """

        self._cheese = cheese

    @property
    def steamid(self):
        """
        Gets the steamid of this InlineResponse2001Profile.
        steamid

        :return: The steamid of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._steamid

    @steamid.setter
    def steamid(self, steamid):
        """
        Sets the steamid of this InlineResponse2001Profile.
        steamid

        :param steamid: The steamid of this InlineResponse2001Profile.
        :type: str
        """

        self._steamid = steamid

    @property
    def avatar(self):
        """
        Gets the avatar of this InlineResponse2001Profile.
        avatar

        :return: The avatar of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this InlineResponse2001Profile.
        avatar

        :param avatar: The avatar of this InlineResponse2001Profile.
        :type: str
        """

        self._avatar = avatar

    @property
    def avatarmedium(self):
        """
        Gets the avatarmedium of this InlineResponse2001Profile.
        avatarmedium

        :return: The avatarmedium of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._avatarmedium

    @avatarmedium.setter
    def avatarmedium(self, avatarmedium):
        """
        Sets the avatarmedium of this InlineResponse2001Profile.
        avatarmedium

        :param avatarmedium: The avatarmedium of this InlineResponse2001Profile.
        :type: str
        """

        self._avatarmedium = avatarmedium

    @property
    def avatarfull(self):
        """
        Gets the avatarfull of this InlineResponse2001Profile.
        avatarfull

        :return: The avatarfull of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._avatarfull

    @avatarfull.setter
    def avatarfull(self, avatarfull):
        """
        Sets the avatarfull of this InlineResponse2001Profile.
        avatarfull

        :param avatarfull: The avatarfull of this InlineResponse2001Profile.
        :type: str
        """

        self._avatarfull = avatarfull

    @property
    def profileurl(self):
        """
        Gets the profileurl of this InlineResponse2001Profile.
        profileurl

        :return: The profileurl of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._profileurl

    @profileurl.setter
    def profileurl(self, profileurl):
        """
        Sets the profileurl of this InlineResponse2001Profile.
        profileurl

        :param profileurl: The profileurl of this InlineResponse2001Profile.
        :type: str
        """

        self._profileurl = profileurl

    @property
    def last_login(self):
        """
        Gets the last_login of this InlineResponse2001Profile.
        last_login

        :return: The last_login of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this InlineResponse2001Profile.
        last_login

        :param last_login: The last_login of this InlineResponse2001Profile.
        :type: str
        """

        self._last_login = last_login

    @property
    def loccountrycode(self):
        """
        Gets the loccountrycode of this InlineResponse2001Profile.
        loccountrycode

        :return: The loccountrycode of this InlineResponse2001Profile.
        :rtype: str
        """
        return self._loccountrycode

    @loccountrycode.setter
    def loccountrycode(self, loccountrycode):
        """
        Sets the loccountrycode of this InlineResponse2001Profile.
        loccountrycode

        :param loccountrycode: The loccountrycode of this InlineResponse2001Profile.
        :type: str
        """

        self._loccountrycode = loccountrycode

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
        if not isinstance(other, InlineResponse2001Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
