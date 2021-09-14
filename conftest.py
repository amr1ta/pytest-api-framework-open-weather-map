import pytest

import owm_client


@pytest.fixture(scope="class")
def apiclient():
    return owm_client.OpenWeatherMap_Client()


def pytest_addoption(parser):
    parser.addoption("--city", action="store", default="London,UK")


@pytest.fixture(scope="class")
def city(pytestconfig):
    return pytestconfig.getoption("city")
