# API testing using pytest and requests

## Target API service: https://samples.openweathermap.org/

## Instructions to execute

```
pip3 install -r requirements.txt
pytest -s --city "London,UK"
```

## Test Scenarios Covered

**Scenario 1**

Steps:
1. Manually make a GET request to [this](https://samples.openweathermap.org/data/2.5/history/city?q=London,UK&appid=b1b15ee88fa797225412429c1c50c122a1) URL and capture JSON response.
This step can also be done by `test_get_expected_data` test step of the test case by removing `@pytest.mark.skip`
2. Convert the response to CSV and save the file as expected.csv
3. Programmatically make a GET request to same URL
4. Convert the response to CSV and save the file as actual.csv
5. Now read 5 columns each from expected.csv and actual.csv and write output to output.csv by placing similar rows side by side.

## [Final Report](output.csv)
