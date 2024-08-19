# Help you to make the POST, GET, PATCH, PUT and Delete.

import json
import requests
import pytest


def get_base_end_point():
    with open("/Users/vinuthar/PycharmProjects/ApiAutomationUsingPytestFramework/config/endpoints.json") as json_file:
        properties = json.load(json_file)
        env = properties["environment"]["env"]
        return properties[env]["base_url"]


def get_request(url, params, headers, expected_status_code):
    response = requests.get(url=url, params=params, headers=headers)
    try:
        assert response.status_code == expected_status_code, f"received {response.status_code} but expected is {expected_status_code}"
        return response
    except:
        pytest.fail("Get request Api call Failed")


def post_request(url, params, json, headers, expected_status_code):
    response = requests.post(url=url, params=params, json=json, headers=headers)
    try:
        assert response.status_code == expected_status_code, f"received {response.status_code} but expected is {expected_status_code}"
        return response
    except:
        pytest.fail("Post request Api call Failed")


def put_request(url, params, json, headers, expected_status_code):
    response = requests.put(url=url, params=params, json=json, headers=headers)
    try:
        assert response.status_code == expected_status_code, f"received {response.status_code} but expected is {expected_status_code}"
        return response
    except:
        pytest.fail("Put request Api call Failed")


def delete_request(url, params,json, headers):
    response = requests.delete(url=url, params=params, headers=headers)
    if json is True:
        return response.json()
    return response

