import requests

"""
    This app simulated another backend app usign our API (Consumer)
    The Provider will be our machine learning App.
    
    This is Consumer-side test, after we execute it with
    "
        pytest (...).py
    "
    consumer-provider.json file is generated so we can use it on providers side to validate provider service. Warning: it is not generated if you run test inm VS code.
    "
        pact-verifier --provider-base-url=http://localhost:5000 --pact-url=consumer-provider.json
    "

"""


def verbose(function):
    """
        Extends request with printing results
    """

    def wrapper(arg):
        response = function(arg)
        print(f" Response received -- {response.json()}")
        return response

    return wrapper


@verbose
def getPrediction(dataRow):
    """Predict mpg value"""
    url = f"http://localhost:5000/api"
    response = requests.post(url, json=dataRow)
    return response


getPrediction(
    {  # we need double quotation marks here as it will become JSON
        "cylinders": 7,
        "displacement": 77,
        "horsepower": 200,
        "weight": 1900,
        "year": 80,
        "origin": 3,
    }
)

