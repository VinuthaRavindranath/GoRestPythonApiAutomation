import json
import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="staging")


def update_env(config):
    with open("/Users/vinuthar/PycharmProjects/EndToEndApiAutomation/config/endpoints.json") as jsonFile:
        data = json.load(jsonFile)
        data['environment']['env'] = config.getoption("--host").lower
        jsonFile.close()


@pytest.hookimpl
def pytest_configure(config):
    update_env(config)
