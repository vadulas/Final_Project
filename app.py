#imports
from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
import pickle
from data_prep import prep_data
from werkzeug.utils import secure_filename
import pandas as pd
import os

UPLOAD_FOLDER = 'uploaded-files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    content  = dict(request.files)
    print("This works")
    print(content)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'fileinput' not in request.files:
            # flash('No file part')
            # return redirect(request.url)
            return "inpput file not in request.files"
        file = request.files['fileinput']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            # flash('No selected file')
            # return redirect(request.url)
            return "file.filename was empty"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(df)




            # return redirect(url_for('download_file', name=filename))


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
    app.run(debug=True)