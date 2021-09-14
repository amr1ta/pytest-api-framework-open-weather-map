import logging

import pytest

from utils import csv_util

LOGGER = logging.getLogger(__name__)

class Test_OpenWeatherMap:
    @pytest.mark.skip(reason="Expected data fetched manually")
    def test_get_expected_data(self, apiclient, city):
        status_code, response = apiclient.get_weather_data_by_city(city)
        assert status_code == 200, LOGGER.error("GET Request failed")
        csv_util.write_json_to_csv(response, csvfile="expected.csv")

    def test_get_actual_data(self, apiclient, city):
        status_code, response = apiclient.get_weather_data_by_city(city)
        assert status_code == 200, LOGGER.error("GET Request failed")
        csv_util.write_json_to_csv(response, csvfile="actual.csv")

    def test_generate_report(self):
        csv_util.generate_report(
            expected="expected.csv",
            actual="actual.csv",
            output="output.csv",
            limit_columns=5,
        )
        LOGGER.info("Report generated successfully")
