from pact import Verifier
import pathlib
import os


folder = pathlib.Path(__file__).parent.resolve()


def test_self_with_consumer_generated_contract(
    baseURL="http://localhost:5000",
    contract_path=os.path.join(folder, "../consumer/consumer-provider.json"),
):
    """
        Verifies the consumer-provider.json contract against the  provider URL
        Provider can be sent the contract and continuously check their side
    """

    verifier = Verifier(provider="PredictorApp", provider_base_url=baseURL)
    success, logs = verifier.verify_pacts(contract_path)
    assert success == 0
