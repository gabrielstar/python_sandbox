import atexit
import requests
from pact import Consumer, Provider, Like, Format

pact = Consumer("Consumer").has_pact_with(Provider("Provider"))
pact.start_service()
atexit.register(pact.stop_service)

"""
    Consumer tests acdcording to the contract so it is sure that when it switches to real service all works

    1.Define the Consumer and Provider objects that describe API endpoint and expected payload
    2.Define the setup criteria for the Provider
    3.Define the Consumer request using Pact
    4.Define how the provider is expected to respond using Pact
    5.Assert the response to validate the contract
"""


def test_get_simple_prediction(request_body):
    # this is provider's contract - that thing will be returned, can be taekn form pact file
    expected = {
        "errors": [],
        "id": Format().uuid,
        "mpg": Like(33.0111),
    }

    (
        pact.given("We have correct data set for prediction")
        .upon_receiving("a request for prediction")
        .with_request(
            method="POST",
            path="/api",
            body=request_body,
            headers={"Content-Type": "application/json"},
        )
        .will_respond_with(
            status=200, headers={"Content-Type": "application/json"}, body=expected
        )
    )

    with pact:
        result = requests.post(f"{pact.uri}/api", json=request_body)
        pact.verify()
