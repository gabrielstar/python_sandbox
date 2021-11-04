# fist install tensorflow https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/ using anaconda navigator for desired environment
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
import io
import os
import requests
import numpy as np
from sklearn import metrics

# data frame, read it from CSV with pandas
df = pd.read_csv(r"C:\Users\gstarczewski\machine\auto-mpg.csv", na_values=["NA", "?"])
df.head(10)


## DATA PREP
# check if we have null values
df.isnull().sum()
# replace non existent values with medians
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())
# verify they are gone
df.isnull().sum()
# partition data into what we want as input and output (predicted value)
x = df[["cylinders", "displacement", "horsepower", "weight", "year", "origin"]].values
y = df["mpg"].values
# values function converts data into numpy arrays
type(y)
# we split data into train and test set, for reproducibility we fix random state used by random numbers generators
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)  # will contains [rows nr,columns nr]
x_train.shape


##MODEL DEFINITION AND TRAINING
# we use ceratin model based on neural networks e.g. 2 dense layers and output
model = Sequential()
# first network layer required dimension size - it is input layer
model.add(Dense(25, input_dim=x.shape[1], activation="relu"))
# next ones do not require dimension
model.add(Dense(10, activation="relu"))
model.add(Dense(1))  # output value we want

# compile model and tell it how it should learn
# we reduce the loss to be as small as possible using adam optimizer, there are many optimizers
model.compile(loss="mean_squared_error", optimizer="adam")
# monitor learning process, when to stop when in 5 learning rounds we do not get better value imrpovement as 0.001
# if you do not achieve 0.001 improvement in 5 rounds stop and restore best weights achieved
# loss and validation loss
monitor = EarlyStopping(
    monitor="val_loss",
    min_delta=1e-3,
    patience=5,
    verbose=1,
    mode="auto",
    restore_best_weights=True,
)
# fit model
model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    callbacks=[monitor],
    verbose=2,
    epochs=1000,
)
# the result should be the best model weights, the structure, options we chose and data set matters
