#imports
from flask import Flask, render_template, redirect, url_for, request, jsonify
import pickle
from data_prep import prep_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    content  = request.json

    # Load model
    model = pickle.load(open('abc.pkl', 'rb'))

    data = prep_data(content)
    prediction = model.predict(data)
    print(prediction)
     # Create labels based on predictions (assuming threshold of 0.5)
    probability = [1 if i >= 0.5 else 0 for i in prediction]

    if probability == 1: 
        label = "Player will be an 'All Star'"
    else:
        label = "Player will not be an 'All Star'"
    # Return the required result
    return label

    


if __name__ == "__main__":
    app.run()