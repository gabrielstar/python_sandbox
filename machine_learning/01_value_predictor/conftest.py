import pytest
from application import init_app
from application import prediction_service

# fixtures will be visible to all pytest files w/o explicit imports
@pytest.fixture
def request_body():
    json = {  # we need double quotation marks here as it will become JSON
        "cylinders": 7,
        "displacement": 77,
        "horsepower": 200,
        "weight": 1900,
        "year": 80,
        "origin": 3,
    }
    return json


@pytest.fixture
def client():
    app = init_app()
    with app.test_client() as client:
        with app.app_context():
            pass  # here we can do stuff such as db seeding, pre-auth etc
        yield client


@pytest.fixture
def predict():
    return prediction_service.predict
