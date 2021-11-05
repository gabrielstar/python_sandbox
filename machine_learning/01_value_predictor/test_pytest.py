import requests
import json

json = {  # we need double quotation marks here
    "cylinders": 7,
    "displacement": 77,
    "horsepower": 200,
    "weight": 1900,
    "year": 80,
    "origin": 3,
}

base_url = "http://localhost:5001/api"


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def test_posting_correct_data_returns_status_code_200():
    r = requests.post(base_url, json=json)
    assert r.status_code == 200


def test_posting_correct_data_returns_float_value_prediction():
    r = requests.post(base_url, json=json)
    prediction = r.json()["mpg"]
    errors = r.json()["errors"]
    assert isfloat(prediction)
    assert float(prediction) > 0
    assert not errors


def test_posting_incorrect_data_returns_status_code_200_and_errors():
    invalid_json = json.copy()
    del invalid_json["year"]
    r = requests.post(base_url, json=invalid_json)
    errors = r.json()["errors"]
    assert r.status_code == 200
    assert errors
