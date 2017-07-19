# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 15.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.hero_stats_api import HeroStatsApi


class TestHeroStatsApi(unittest.TestCase):
    """ HeroStatsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.hero_stats_api.HeroStatsApi()

    def tearDown(self):
        pass

    def test_hero_stats_get(self):
        """
        Test case for hero_stats_get

        GET /heroStats
        """
        pass


if __name__ == '__main__':
    unittest.main()