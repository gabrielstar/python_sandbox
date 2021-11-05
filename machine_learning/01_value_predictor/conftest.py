import pytest

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

