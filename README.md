# od-python

This project is generated for OpenDota api using swagger.

What I do:
```sh
wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.3/swagger-codegen-cli-2.2.3.jar -O swagger-codegen-cli.jar
java -jar swagger-codegen-cli.jar generate -i https://api.opendota.com/api -l python -o /tmp/od-python/ --git-repo-id od-python --git-user-id seraphli --config config.json
```

<<<<<<< HEAD
**NB**: Recommend using python 3, unless you want to deal with ssl error.

# Introduction This API provides Dota 2 related data. Please keep request rate to approximately 3/s. 
=======
## Introduction

**This API provides Dota 2 related data. Please keep request rate to approximately 3/s.**
>>>>>>> fc74b23137315f58785463579e06169cb9dc7c57

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 15.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/seraphli/od-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/seraphli/od-python.git`)

Then import the package:
```python
import od_python 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import od_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import od_python
from od_python.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = od_python.BenchmarksApi()
hero_id = 'hero_id_example' # str | Hero ID

try:
    # GET /benchmarks
    api_response = api_instance.benchmarks_get(hero_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->benchmarks_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.opendota.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BenchmarksApi* | [**benchmarks_get**](docs/BenchmarksApi.md#benchmarks_get) | **GET** /benchmarks | GET /benchmarks
*DistributionsApi* | [**distributions_get**](docs/DistributionsApi.md#distributions_get) | **GET** /distributions | GET /distributions
*ExplorerApi* | [**explorer_get**](docs/ExplorerApi.md#explorer_get) | **GET** /explorer | GET /explorer
*HealthApi* | [**health_get**](docs/HealthApi.md#health_get) | **GET** /health | GET /health
*HeroStatsApi* | [**hero_stats_get**](docs/HeroStatsApi.md#hero_stats_get) | **GET** /heroStats | GET /heroStats
*HeroesApi* | [**heroes_get**](docs/HeroesApi.md#heroes_get) | **GET** /heroes | GET /heroes
*LeaguesApi* | [**leagues_get**](docs/LeaguesApi.md#leagues_get) | **GET** /leagues | GET /leagues
*MatchesApi* | [**matches_match_id_get**](docs/MatchesApi.md#matches_match_id_get) | **GET** /matches/{match_id} | GET /matches/{match_id}
*MetadataApi* | [**metadata_get**](docs/MetadataApi.md#metadata_get) | **GET** /metadata | GET /metadata
*PlayersApi* | [**players_account_id_counts_get**](docs/PlayersApi.md#players_account_id_counts_get) | **GET** /players/{account_id}/counts | GET /players/{account_id}/counts
*PlayersApi* | [**players_account_id_get**](docs/PlayersApi.md#players_account_id_get) | **GET** /players/{account_id} | GET /players/{account_id}
*PlayersApi* | [**players_account_id_heroes_get**](docs/PlayersApi.md#players_account_id_heroes_get) | **GET** /players/{account_id}/heroes | GET /players/{account_id}/heroes
*PlayersApi* | [**players_account_id_histograms_field_get**](docs/PlayersApi.md#players_account_id_histograms_field_get) | **GET** /players/{account_id}/histograms/{field} | GET /players/{account_id}/histograms
*PlayersApi* | [**players_account_id_matches_get**](docs/PlayersApi.md#players_account_id_matches_get) | **GET** /players/{account_id}/matches | GET /players/{account_id}/matches
*PlayersApi* | [**players_account_id_peers_get**](docs/PlayersApi.md#players_account_id_peers_get) | **GET** /players/{account_id}/peers | GET /players/{account_id}/peers
*PlayersApi* | [**players_account_id_pros_get**](docs/PlayersApi.md#players_account_id_pros_get) | **GET** /players/{account_id}/pros | GET /players/{account_id}/pros
*PlayersApi* | [**players_account_id_rankings_get**](docs/PlayersApi.md#players_account_id_rankings_get) | **GET** /players/{account_id}/rankings | GET /players/{account_id}/rankings
*PlayersApi* | [**players_account_id_ratings_get**](docs/PlayersApi.md#players_account_id_ratings_get) | **GET** /players/{account_id}/ratings | GET /players/{account_id}/ratings
*PlayersApi* | [**players_account_id_recent_matches_get**](docs/PlayersApi.md#players_account_id_recent_matches_get) | **GET** /players/{account_id}/recentMatches | GET /players/{account_id}/recentMatches
*PlayersApi* | [**players_account_id_refresh_post**](docs/PlayersApi.md#players_account_id_refresh_post) | **POST** /players/{account_id}/refresh | POST /players/{account_id}/refresh
*PlayersApi* | [**players_account_id_totals_get**](docs/PlayersApi.md#players_account_id_totals_get) | **GET** /players/{account_id}/totals | GET /players/{account_id}/totals
*PlayersApi* | [**players_account_id_wardmap_get**](docs/PlayersApi.md#players_account_id_wardmap_get) | **GET** /players/{account_id}/wardmap | GET /players/{account_id}/wardmap
*PlayersApi* | [**players_account_id_wl_get**](docs/PlayersApi.md#players_account_id_wl_get) | **GET** /players/{account_id}/wl | GET /players/{account_id}/wl
*PlayersApi* | [**players_account_id_wordcloud_get**](docs/PlayersApi.md#players_account_id_wordcloud_get) | **GET** /players/{account_id}/wordcloud | GET /players/{account_id}/wordcloud
*ProMatchesApi* | [**pro_matches_get**](docs/ProMatchesApi.md#pro_matches_get) | **GET** /proMatches | GET /proMatches
*ProPlayersApi* | [**pro_players_get**](docs/ProPlayersApi.md#pro_players_get) | **GET** /proPlayers | GET /proPlayers
*PublicMatchesApi* | [**public_matches_get**](docs/PublicMatchesApi.md#public_matches_get) | **GET** /publicMatches | GET /publicMatches
*RankingsApi* | [**rankings_get**](docs/RankingsApi.md#rankings_get) | **GET** /rankings | GET /rankings
*RecordsApi* | [**records_field_get**](docs/RecordsApi.md#records_field_get) | **GET** /records/{field} | GET /records/{field}
*ReplaysApi* | [**replays_get**](docs/ReplaysApi.md#replays_get) | **GET** /replays | GET /replays
*RequestApi* | [**request_job_id_get**](docs/RequestApi.md#request_job_id_get) | **GET** /request/{jobId} | GET /request/{jobId}
*RequestApi* | [**request_match_id_post**](docs/RequestApi.md#request_match_id_post) | **POST** /request/{match_id} | POST /request/{match_id}
*SchemaApi* | [**schema_get**](docs/SchemaApi.md#schema_get) | **GET** /schema | GET /schema
*SearchApi* | [**search_get**](docs/SearchApi.md#search_get) | **GET** /search | GET /search
*StatusApi* | [**status_get**](docs/StatusApi.md#status_get) | **GET** /status | GET /status
*TeamsApi* | [**teams_get**](docs/TeamsApi.md#teams_get) | **GET** /teams | GET /teams


## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20017Cheese](docs/InlineResponse20017Cheese.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20018CountryMmr](docs/InlineResponse20018CountryMmr.md)
 - [InlineResponse20018CountryMmrRows](docs/InlineResponse20018CountryMmrRows.md)
 - [InlineResponse20018Mmr](docs/InlineResponse20018Mmr.md)
 - [InlineResponse20018MmrFields](docs/InlineResponse20018MmrFields.md)
 - [InlineResponse20018MmrRows](docs/InlineResponse20018MmrRows.md)
 - [InlineResponse20018MmrSum](docs/InlineResponse20018MmrSum.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2001MmrEstimate](docs/InlineResponse2001MmrEstimate.md)
 - [InlineResponse2001Profile](docs/InlineResponse2001Profile.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20020Rankings](docs/InlineResponse20020Rankings.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20021Result](docs/InlineResponse20021Result.md)
 - [InlineResponse20021ResultGoldPerMin](docs/InlineResponse20021ResultGoldPerMin.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse200Players](docs/InlineResponse200Players.md)
 - [PlayersaccountIdmatchesHeroes](docs/PlayersaccountIdmatchesHeroes.md)
 - [PlayersaccountIdmatchesHeroesPlayerSlot](docs/PlayersaccountIdmatchesHeroesPlayerSlot.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



