import pytest
import json
import io
import os
from SpyCloudEnterpriseEnrichment import Client, command_helper_function, breaches_list_command, \
    get_breach_data_by_id_command, get_breach_data_by_domain_command, \
    get_breach_data_by_passwords_command, get_watchlist_data_command, \
    get_breach_data_by_username_command, \
    get_breach_data_by_ip_address_command, \
    get_breach_data_by_email_address_command, \
    get_compass_application_data_command, get_compass_device_data_command, \
    compass_data_list_command, compass_device_list_command


def util_load_json(path):
    with io.open(path, mode='r') as f:
        return json.loads(f.read())


BREACH_LIST_RESPONSE = util_load_json('test_data/breach_list.json')
BREACH_DATA_BY_INDICATOR = util_load_json(
    'test_data/breach_data_by_indicator.json')

client = Client(
    base_url="http://test.com/",
    apikey="test_123",
    proxy=False,
    verify=False
)


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_LIST_RESPONSE, BREACH_LIST_RESPONSE)])
def test_command_helper_function(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'limit': 5
    }
    endpoint = 'breach/catalog'
    title_string = 'Breach List'
    result, title = command_helper_function(client, endpoint, args,
                                            title_string)
    assert result == expected.get('results')
    assert title == title_string


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_LIST_RESPONSE, BREACH_LIST_RESPONSE)])
def test_breaches_list_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'limit': 5
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_list_readable_output.md"),
              'r') as f:
        readable_output = f.read()
    response = breaches_list_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_LIST_RESPONSE, BREACH_LIST_RESPONSE)])
def test_get_breache_data_by_id_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'id': 12345
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_data_by_id.md"), 'r') as f:
        readable_output = f.read()
    response = get_breach_data_by_id_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_breach_data_by_domain_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'domain': 'abc.com'
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_data_by_domain.md"),
              'r') as f:
        readable_output = f.read()
    response = get_breach_data_by_domain_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_breach_data_by_username_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'username': 'abc'
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_data_by_username.md"),
              'r') as f:
        readable_output = f.read()
    response = get_breach_data_by_username_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_breach_data_by_ip_address_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'ip': '1.1.1.1'
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_data_by_ip_address.md"),
              'r') as f:
        readable_output = f.read()
    response = get_breach_data_by_ip_address_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_breach_data_by_email_address_command(mocker, raw_response,
                                                  expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'ip': '1.1.1.1'
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_data_by_email_address.md"),
              'r') as f:
        readable_output = f.read()
    response = get_breach_data_by_email_address_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_breach_data_by_passwords_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'password': 'password'
    }
    with open(os.path.join("test_data",
                           "readable_output/breach_data_by_password.md"),
              'r') as f:
        readable_output = f.read()
    response = get_breach_data_by_passwords_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_watchlist_data_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'limit': '5'
    }
    with open(os.path.join("test_data",
                           "readable_output/watchlist_data.md"), 'r') as f:
        readable_output = f.read()
    response = get_watchlist_data_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')[:5]


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_compass_device_data_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'infected_machine_id': '12345'
    }
    with open(os.path.join("test_data",
                           "readable_output/compass_device_data.md"), 'r') as f:
        readable_output = f.read()
    response = get_compass_device_data_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_compass_data_list_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'infected_machine_id': '12345'
    }
    with open(os.path.join("test_data",
                           "readable_output/compass_data_list.md"), 'r') as f:
        readable_output = f.read()
    response = compass_data_list_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_compass_device_list_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'limit': '5'
    }
    with open(os.path.join("test_data",
                           "readable_output/compass_device_list.md"), 'r') as f:
        readable_output = f.read()
    response = compass_device_list_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')[:5]


@pytest.mark.parametrize('raw_response, expected',
                         [(BREACH_DATA_BY_INDICATOR, BREACH_DATA_BY_INDICATOR)])
def test_get_compass_application_data_command(mocker, raw_response, expected):
    mocker.patch.object(client, 'query_spy_cloud_api',
                        side_effect=[raw_response])
    args = {
        'target_application': 'abcd'
    }
    with open(os.path.join("test_data",
                           "readable_output/compass_application_data.md"),
              'r') as f:
        readable_output = f.read()
    response = get_compass_application_data_command(client, args)
    context_response = response.to_context()['Contents']
    assert response.readable_output == readable_output
    assert context_response == expected.get('results')


def test_query_spy_cloud_api_success(requests_mock):
    endpoint = 'compass/device'
    req_url = f'{client._base_url}{endpoint}'
    requests_mock.get(req_url, json=BREACH_LIST_RESPONSE)
    response = client.query_spy_cloud_api(endpoint, {})
    assert response == BREACH_LIST_RESPONSE
