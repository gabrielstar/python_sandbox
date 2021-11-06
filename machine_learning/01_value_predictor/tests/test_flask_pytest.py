"""
    We can instantiate an app with desired configuration for the test
"""


def test_flask_when_correct_data_is_sent_status_code_is_200_and_prediction_is_returned(
    request_body, client
):
    response = client.post("/api", json=request_body, follow_redirects=False)
    json_response = response.get_json()
    assert response.status_code == 200
    assert json_response["mpg"]
