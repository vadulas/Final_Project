#imports
import os
from flask import Flask, render_template, request
import pickle
from data_prep import prep_data
from werkzeug.utils import secure_filename
import pandas as pd

app_dir = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(app_dir, "uploaded-files")
# ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/requirements")
def reqs():
    return render_template("requirements.html")


@app.route('/predict', methods=['GET','POST'])
def predict():
    content  = request.files['file']
    # print(content)

    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)

        df = pd.read_csv(path)
        #return df.to_html()


    # Load model
    model = pickle.load(open('lr.pkl', 'rb'))

    data = prep_data(df)

    player = df['Player'][0]
    print(player)
    prediction = model.predict(data)
    print(prediction)
     # Create labels based on predictions (assuming threshold of 0.5)
    probability = [1 if i >= 0.5 else 0 for i in prediction]

    if probability == 1: 
        label =f"{player} will be an 'All Star' {probability}"
    else:
        label = f"{player} will not be an 'All Star' {probability}"
    # Return the required result
    return label

    
if __name__ == "__main__":
    app.run(debug=True)