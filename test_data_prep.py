import pandas as pd
from flask import request, jsonify, Blueprint
import pickle
from data_prep import prep_data


# Load model
model = pickle.load(open('abc.pkl', 'rb'))

test_data = pd.read_csv("test.csv")

# Prepare the data for model
data = prep_data(test_data)
prediction = model.predict(data)

print(prediction)
