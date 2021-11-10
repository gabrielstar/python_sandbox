import os
import uuid

import numpy as np
from flask import Blueprint, jsonify, request, send_from_directory, render_template
from tensorflow.keras.models import load_model

expected = {
    "cylinders": {"min": 3, "max": 8},
    "displacement": {"min": 68, "max": 455},
    "horsepower": {"min": 46, "max": 230},
    "weight": {"min": 1613, "max": 5140},
    "year": {"min": 70, "max": 82},
    "origin": {"min": 1, "max": 3},
}
file_path = os.path.abspath(os.path.dirname(__file__))
# model is an artifact because we can train it
model = load_model(os.path.join(file_path, "model", "mpg_model.h5"))
print(model.summary())

# blueprints are ways to divide app into smaller pieces and use in app factory
api = Blueprint("api", __name__)


@api.route("/app.js", methods=["GET", "OPTIONS"])
def send_js():
    return send_from_directory("templates/ui", "app.js")


@api.route("/", methods=["GET", "OPTIONS"])
def index():
    return render_template("ui/index.html")


@api.route("/api", methods=["POST"])
def mpg_prediction():
    content = request.json
    errors = []
    for name in content:
        if name in expected:
            expected_min = expected[name]["min"]
            expected_max = expected[name]["max"]
            value = content[name]
            if value < expected_min or value > expected_max:
                errors.append(
                    f"{name} is out of bounds, {value} outside of {expected_min}, {expected_max}"
                )
        else:
            errors.append(f"Unexpected field {name}")
    for name in expected:
        if name not in content:
            errors.append(f"Missing value {name}")

    if len(errors) < 1:
        x = np.zeros((1, 6))
        x[0, 0] = content["cylinders"]
        x[0, 1] = content["displacement"]
        x[0, 2] = content["horsepower"]
        x[0, 3] = content["weight"]
        x[0, 4] = content["year"]
        x[0, 5] = content["origin"]

        prediction = model.predict(x)
        mpg = float(prediction[0])
        response = {"id": str(uuid.uuid4()), "mpg": mpg, "errors": errors}
    else:
        response = {"id": str(uuid.uuid4()), "errors": errors}
    return jsonify(response)
