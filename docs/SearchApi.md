# od_python.SearchApi

All URIs are relative to *https://api.opendota.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | GET /search


# **search_get**
> list[InlineResponse20018] search_get(q)

GET /search

Search players by personaname.

### Example 
```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.SearchApi()
q = 'q_example' # str | Search string

try: 
    # GET /search
    api_response = api_instance.search_get(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search string | 

### Return type

[**list[InlineResponse20018]**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

