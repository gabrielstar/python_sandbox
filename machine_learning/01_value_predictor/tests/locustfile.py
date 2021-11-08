from locust import HttpUser, task


class PredictionUser(HttpUser):
    json = {  # we need double quotation marks here as it will become JSON
        "cylinders": 7,
        "displacement": 77,
        "horsepower": 200,
        "weight": 1900,
        "year": 80,
        "origin": 3,
    }
    host = "http://localhost:5000"

    @task
    def make_prediction(self):
        self.client.post("/api", json=self.json)
