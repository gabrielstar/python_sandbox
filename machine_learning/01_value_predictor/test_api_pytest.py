import requests

# https://www.numpyninja.com/post/pytest-a-beginner-guide
# https://testdriven.io/blog/flask-pytest/

base_url = "http://localhost:5001/api"


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def test_posting_correct_data_returns_status_code_200(request_body):
    r = requests.post(base_url, json=request_body)
    assert r.status_code == 200


def test_posting_correct_data_returns_float_value_prediction(request_body):
    """
    GIVEN ...
    WHEN ...
    THEN ...
    """
    r = requests.post(base_url, json=request_body)
    prediction = r.json()["mpg"]
    errors = r.json()["errors"]
    assert isfloat(prediction)
    assert float(prediction) > 0
    assert not errors


def test_posting_incorrect_data_returns_status_code_200_and_errors(request_body):
    invalid_json = request_body.copy()
    del invalid_json["year"]
    r = requests.post(base_url, json=invalid_json)
    errors = r.json()["errors"]
    assert r.status_code == 200
    assert errors


def test_posting_additional_data_column_throws_errors(request_body):
    invalid_json = request_body.copy()
    invalid_json["unexpected_column"] = 2
    r = requests.post(base_url, json=invalid_json)
    errors = r.json()["errors"]
    assert r.status_code == 200
    assert errors
