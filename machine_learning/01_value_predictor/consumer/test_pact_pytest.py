import atexit
import requests
from pact import Consumer, Provider, Like, Format, Verifier

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


def test_consumer_get_simple_prediction(request_body):
    """
        Generates the consumer-provider.json contract
    """
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
            status=200,
            headers={"Content-Type": "application/json"},
            body=expected,
        )
    )

    with pact:
        requests.post(f"{pact.uri}/api", json=request_body)
        pact.verify()


def test_provider_with_generated_contract(baseURL="http://localhost:5000"):
    """
        Verifies the consumer-provider.json contract against the  provider URL
        Provider can be sent the contract and continuously check their side
    """

    verifier = Verifier(provider="PredictorApp", provider_base_url=baseURL)
    success, logs = verifier.verify_pacts("consumer-provider.json")
    assert success == 0
