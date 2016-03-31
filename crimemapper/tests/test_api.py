
import pytest
import requests
from requests import Response, HTTPError
try:
    from unittest.mock import MagicMock, Mock
    from unittest.mock import patch
except:
    from mock import MagicMock, Mock
    from mock import patch

import pytest
import requests
from requests import Response, HTTPError
import json
from unittest.mock import MagicMock, Mock
from unittest.mock import patch
from sodapy import Socrata
try:
    from unittest import mock
except ImportError:
    import mock

RESPONSE_200_DATA = [{
    'census_tract_2000': '1900.1012',
    'date_reported': '2016-03-10T08:18:00',
    'district_sector': 'L',
    'general_offense_number': '201684521',
    'hundred_block_location': '2XX BLOCK OF NE 94 ST',
    'latitude': '47.696815491',
    'location': {
        'latitude': '47.696815491',
        'longitude': '-122.327774048',
        'needs_recoding': False
    },
    'longitude': '-122.327774048',
    'occurred_date_or_date_range_start': '1990-01-01T00:00:00',
    'occurred_date_range_end': '2016-03-10T08:00:00',
    'offense_code': 'X',
    'offense_code_extension': '21',
    'offense_type': 'DISTURBANCE-OTH',
    'rms_cdw_id': '700713',
    'summarized_offense_description': 'DISTURBANCE',
    'summary_offense_code': 'X',
    'zone_beat': 'L2'
}]

CLEANED_DATA = [{
    'census_tract_2000': '1900.1012',
    'date_reported': '2016-03-10T08:18:00',
    'district_sector': 'L',
    'general_offense_number': '201684521',
    'hundred_block_location': '2XX BLOCK OF NE 94 ST',
    'latitude': '47.696815491',
    'location': {
        'latitude': '47.696815491',
        'longitude': '-122.327774048',
        'needs_recoding': False
    },
    'longitude': '-122.327774048',
    'occurred_date_or_date_range_start': '1990-01-01T00:00:00',
    'occurred_date_range_end': '2016-03-10T08:00:00',
    'offense_code': None,
    'offense_code_extension': '21',
    'offense_type': 'DISTURBANCE-OTH',
    'rms_cdw_id': '700713',
    'summarized_offense_description': 'DISTURBANCE',
    'summary_offense_code': None,
    'zone_beat': 'L2'
}]


@mock.patch('crimemapper.api.Socrata')
def test_call_api_200(socrata):
    """Test calling url and getting reponse back without raising error."""
    from crimemapper.api import call_api
    mocked = socrata().get
    mocked.return_value = RESPONSE_200_DATA
    assert call_api()[0] == RESPONSE_200_DATA[0]


@mock.patch('crimemapper.api.Socrata')
def test_call_api_connection_error(socrata):
    """Test Call Api with connection error."""
    from crimemapper.api import call_api
    mocked = socrata().get
    mocked.side_effect = ConnectionError
    with pytest.raises(ConnectionError):
        call_api()


@mock.patch('crimemapper.api.Socrata')
def test_call_api_http_error(socrata):
    """Test Call Api with http error."""
    from crimemapper.api import call_api
    mocked = socrata().get
    mocked.side_effect = HTTPError
    with pytest.raises(HTTPError):
        call_api()


def test_clean_crime_entry():
    """Test json data with X replcaed by None."""
    from crimemapper.api import clean_data
    assert clean_data(RESPONSE_200_DATA[0]) == CLEANED_DATA[0]



# def test_populate_db():
#     """Test right entry passed into db."""
#     pass
# #     from crimemapper.api import populate_db
# #     from crimemapper.models import DBSession, Entry
# #     DBSession.add = Mock()
# #     populate_db(CLEANED_DATA)
# #     DBSssion.add.call_args
# #     #call(entries.attr=val)
# #     call()[0]
# #     for key, val in CLEANED_DATA.items():
# #         if key =

