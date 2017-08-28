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


class InlineResponse20016(object):
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
        'id': 'int',
        'name': 'str',
        'localized_name': 'str',
        'img': 'str',
        'icon': 'str',
        'pro_win': 'int',
        'pro_pick': 'int',
        'hero_id': 'int',
        'pro_ban': 'int',
        '_1000_pick': 'int',
        '_1000_win': 'int',
        '_2000_pick': 'int',
        '_2000_win': 'int',
        '_3000_pick': 'int',
        '_3000_win': 'int',
        '_4000_pick': 'int',
        '_4000_win': 'int',
        '_5000_pick': 'int',
        '_5000_win': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'localized_name': 'localized_name',
        'img': 'img',
        'icon': 'icon',
        'pro_win': 'pro_win',
        'pro_pick': 'pro_pick',
        'hero_id': 'hero_id',
        'pro_ban': 'pro_ban',
        '_1000_pick': '1000_pick',
        '_1000_win': '1000_win',
        '_2000_pick': '2000_pick',
        '_2000_win': '2000_win',
        '_3000_pick': '3000_pick',
        '_3000_win': '3000_win',
        '_4000_pick': '4000_pick',
        '_4000_win': '4000_win',
        '_5000_pick': '5000_pick',
        '_5000_win': '5000_win'
    }

    def __init__(self, id=None, name=None, localized_name=None, img=None, icon=None, pro_win=None, pro_pick=None, hero_id=None, pro_ban=None, _1000_pick=None, _1000_win=None, _2000_pick=None, _2000_win=None, _3000_pick=None, _3000_win=None, _4000_pick=None, _4000_win=None, _5000_pick=None, _5000_win=None):
        """
        InlineResponse20016 - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._localized_name = None
        self._img = None
        self._icon = None
        self._pro_win = None
        self._pro_pick = None
        self._hero_id = None
        self._pro_ban = None
        self.__1000_pick = None
        self.__1000_win = None
        self.__2000_pick = None
        self.__2000_win = None
        self.__3000_pick = None
        self.__3000_win = None
        self.__4000_pick = None
        self.__4000_win = None
        self.__5000_pick = None
        self.__5000_win = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if localized_name is not None:
          self.localized_name = localized_name
        if img is not None:
          self.img = img
        if icon is not None:
          self.icon = icon
        if pro_win is not None:
          self.pro_win = pro_win
        if pro_pick is not None:
          self.pro_pick = pro_pick
        if hero_id is not None:
          self.hero_id = hero_id
        if pro_ban is not None:
          self.pro_ban = pro_ban
        if _1000_pick is not None:
          self._1000_pick = _1000_pick
        if _1000_win is not None:
          self._1000_win = _1000_win
        if _2000_pick is not None:
          self._2000_pick = _2000_pick
        if _2000_win is not None:
          self._2000_win = _2000_win
        if _3000_pick is not None:
          self._3000_pick = _3000_pick
        if _3000_win is not None:
          self._3000_win = _3000_win
        if _4000_pick is not None:
          self._4000_pick = _4000_pick
        if _4000_win is not None:
          self._4000_win = _4000_win
        if _5000_pick is not None:
          self._5000_pick = _5000_pick
        if _5000_win is not None:
          self._5000_win = _5000_win

    @property
    def id(self):
        """
        Gets the id of this InlineResponse20016.
        id

        :return: The id of this InlineResponse20016.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InlineResponse20016.
        id

        :param id: The id of this InlineResponse20016.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InlineResponse20016.
        name

        :return: The name of this InlineResponse20016.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse20016.
        name

        :param name: The name of this InlineResponse20016.
        :type: str
        """

        self._name = name

    @property
    def localized_name(self):
        """
        Gets the localized_name of this InlineResponse20016.
        localized_name

        :return: The localized_name of this InlineResponse20016.
        :rtype: str
        """
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        """
        Sets the localized_name of this InlineResponse20016.
        localized_name

        :param localized_name: The localized_name of this InlineResponse20016.
        :type: str
        """

        self._localized_name = localized_name

    @property
    def img(self):
        """
        Gets the img of this InlineResponse20016.
        img

        :return: The img of this InlineResponse20016.
        :rtype: str
        """
        return self._img

    @img.setter
    def img(self, img):
        """
        Sets the img of this InlineResponse20016.
        img

        :param img: The img of this InlineResponse20016.
        :type: str
        """

        self._img = img

    @property
    def icon(self):
        """
        Gets the icon of this InlineResponse20016.
        icon

        :return: The icon of this InlineResponse20016.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this InlineResponse20016.
        icon

        :param icon: The icon of this InlineResponse20016.
        :type: str
        """

        self._icon = icon

    @property
    def pro_win(self):
        """
        Gets the pro_win of this InlineResponse20016.
        pro_win

        :return: The pro_win of this InlineResponse20016.
        :rtype: int
        """
        return self._pro_win

    @pro_win.setter
    def pro_win(self, pro_win):
        """
        Sets the pro_win of this InlineResponse20016.
        pro_win

        :param pro_win: The pro_win of this InlineResponse20016.
        :type: int
        """

        self._pro_win = pro_win

    @property
    def pro_pick(self):
        """
        Gets the pro_pick of this InlineResponse20016.
        pro_pick

        :return: The pro_pick of this InlineResponse20016.
        :rtype: int
        """
        return self._pro_pick

    @pro_pick.setter
    def pro_pick(self, pro_pick):
        """
        Sets the pro_pick of this InlineResponse20016.
        pro_pick

        :param pro_pick: The pro_pick of this InlineResponse20016.
        :type: int
        """

        self._pro_pick = pro_pick

    @property
    def hero_id(self):
        """
        Gets the hero_id of this InlineResponse20016.
        hero_id

        :return: The hero_id of this InlineResponse20016.
        :rtype: int
        """
        return self._hero_id

    @hero_id.setter
    def hero_id(self, hero_id):
        """
        Sets the hero_id of this InlineResponse20016.
        hero_id

        :param hero_id: The hero_id of this InlineResponse20016.
        :type: int
        """

        self._hero_id = hero_id

    @property
    def pro_ban(self):
        """
        Gets the pro_ban of this InlineResponse20016.
        pro_ban

        :return: The pro_ban of this InlineResponse20016.
        :rtype: int
        """
        return self._pro_ban

    @pro_ban.setter
    def pro_ban(self, pro_ban):
        """
        Sets the pro_ban of this InlineResponse20016.
        pro_ban

        :param pro_ban: The pro_ban of this InlineResponse20016.
        :type: int
        """

        self._pro_ban = pro_ban

    @property
    def _1000_pick(self):
        """
        Gets the _1000_pick of this InlineResponse20016.
        1000_pick

        :return: The _1000_pick of this InlineResponse20016.
        :rtype: int
        """
        return self.__1000_pick

    @_1000_pick.setter
    def _1000_pick(self, _1000_pick):
        """
        Sets the _1000_pick of this InlineResponse20016.
        1000_pick

        :param _1000_pick: The _1000_pick of this InlineResponse20016.
        :type: int
        """

        self.__1000_pick = _1000_pick

    @property
    def _1000_win(self):
        """
        Gets the _1000_win of this InlineResponse20016.
        1000_win

        :return: The _1000_win of this InlineResponse20016.
        :rtype: int
        """
        return self.__1000_win

    @_1000_win.setter
    def _1000_win(self, _1000_win):
        """
        Sets the _1000_win of this InlineResponse20016.
        1000_win

        :param _1000_win: The _1000_win of this InlineResponse20016.
        :type: int
        """

        self.__1000_win = _1000_win

    @property
    def _2000_pick(self):
        """
        Gets the _2000_pick of this InlineResponse20016.
        2000_pick

        :return: The _2000_pick of this InlineResponse20016.
        :rtype: int
        """
        return self.__2000_pick

    @_2000_pick.setter
    def _2000_pick(self, _2000_pick):
        """
        Sets the _2000_pick of this InlineResponse20016.
        2000_pick

        :param _2000_pick: The _2000_pick of this InlineResponse20016.
        :type: int
        """

        self.__2000_pick = _2000_pick

    @property
    def _2000_win(self):
        """
        Gets the _2000_win of this InlineResponse20016.
        2000_win

        :return: The _2000_win of this InlineResponse20016.
        :rtype: int
        """
        return self.__2000_win

    @_2000_win.setter
    def _2000_win(self, _2000_win):
        """
        Sets the _2000_win of this InlineResponse20016.
        2000_win

        :param _2000_win: The _2000_win of this InlineResponse20016.
        :type: int
        """

        self.__2000_win = _2000_win

    @property
    def _3000_pick(self):
        """
        Gets the _3000_pick of this InlineResponse20016.
        3000_pick

        :return: The _3000_pick of this InlineResponse20016.
        :rtype: int
        """
        return self.__3000_pick

    @_3000_pick.setter
    def _3000_pick(self, _3000_pick):
        """
        Sets the _3000_pick of this InlineResponse20016.
        3000_pick

        :param _3000_pick: The _3000_pick of this InlineResponse20016.
        :type: int
        """

        self.__3000_pick = _3000_pick

    @property
    def _3000_win(self):
        """
        Gets the _3000_win of this InlineResponse20016.
        3000_win

        :return: The _3000_win of this InlineResponse20016.
        :rtype: int
        """
        return self.__3000_win

    @_3000_win.setter
    def _3000_win(self, _3000_win):
        """
        Sets the _3000_win of this InlineResponse20016.
        3000_win

        :param _3000_win: The _3000_win of this InlineResponse20016.
        :type: int
        """

        self.__3000_win = _3000_win

    @property
    def _4000_pick(self):
        """
        Gets the _4000_pick of this InlineResponse20016.
        4000_pick

        :return: The _4000_pick of this InlineResponse20016.
        :rtype: int
        """
        return self.__4000_pick

    @_4000_pick.setter
    def _4000_pick(self, _4000_pick):
        """
        Sets the _4000_pick of this InlineResponse20016.
        4000_pick

        :param _4000_pick: The _4000_pick of this InlineResponse20016.
        :type: int
        """

        self.__4000_pick = _4000_pick

    @property
    def _4000_win(self):
        """
        Gets the _4000_win of this InlineResponse20016.
        4000_win

        :return: The _4000_win of this InlineResponse20016.
        :rtype: int
        """
        return self.__4000_win

    @_4000_win.setter
    def _4000_win(self, _4000_win):
        """
        Sets the _4000_win of this InlineResponse20016.
        4000_win

        :param _4000_win: The _4000_win of this InlineResponse20016.
        :type: int
        """

        self.__4000_win = _4000_win

    @property
    def _5000_pick(self):
        """
        Gets the _5000_pick of this InlineResponse20016.
        5000_pick

        :return: The _5000_pick of this InlineResponse20016.
        :rtype: int
        """
        return self.__5000_pick

    @_5000_pick.setter
    def _5000_pick(self, _5000_pick):
        """
        Sets the _5000_pick of this InlineResponse20016.
        5000_pick

        :param _5000_pick: The _5000_pick of this InlineResponse20016.
        :type: int
        """

        self.__5000_pick = _5000_pick

    @property
    def _5000_win(self):
        """
        Gets the _5000_win of this InlineResponse20016.
        5000_win

        :return: The _5000_win of this InlineResponse20016.
        :rtype: int
        """
        return self.__5000_win

    @_5000_win.setter
    def _5000_win(self, _5000_win):
        """
        Sets the _5000_win of this InlineResponse20016.
        5000_win

        :param _5000_win: The _5000_win of this InlineResponse20016.
        :type: int
        """

        self.__5000_win = _5000_win

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
        if not isinstance(other, InlineResponse20016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
