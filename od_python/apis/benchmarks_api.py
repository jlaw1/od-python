# coding: utf-8

"""
    OpenDota API

    # Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 

    OpenAPI spec version: 17.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BenchmarksApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def benchmarks_get(self, hero_id, **kwargs):
        """
        GET /benchmarks
        Benchmarks of average stat values for a hero
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.benchmarks_get(hero_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str hero_id: Hero ID (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.benchmarks_get_with_http_info(hero_id, **kwargs)
        else:
            (data) = self.benchmarks_get_with_http_info(hero_id, **kwargs)
            return data

    def benchmarks_get_with_http_info(self, hero_id, **kwargs):
        """
        GET /benchmarks
        Benchmarks of average stat values for a hero
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.benchmarks_get_with_http_info(hero_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str hero_id: Hero ID (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hero_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method benchmarks_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hero_id' is set
        if ('hero_id' not in params) or (params['hero_id'] is None):
            raise ValueError("Missing the required parameter `hero_id` when calling `benchmarks_get`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'hero_id' in params:
            query_params.append(('hero_id', params['hero_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/benchmarks', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20021',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
