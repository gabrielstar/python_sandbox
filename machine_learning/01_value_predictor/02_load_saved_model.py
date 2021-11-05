import os
from tensorflow.keras.models import load_model
import numpy as np

# load model that has been saved before
os.chdir(r"C:\Users\gstarczewski\machine")
model = load_model(os.path.join(os.getcwd(), "mpg_model.h5"))
model.summary()
# create input for prediction
x = np.zeros((1, 6))
x[0, 0] = 8
x[0, 1] = 400
x[0, 2] = 80
x[0, 3] = 2000
x[0, 4] = 19
x[0, 5] = 72

# make a prediction
prediction = model.predict(x)
print(f"predicted value of {float(prediction[0])}")
