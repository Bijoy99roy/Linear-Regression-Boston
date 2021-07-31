from flask import Flask, request, render_template, send_file, redirect, url_for
from predictionValidation import PredictionValidation
from prediction_data_validation.prediction_data_validation import PredictionDataValidation
from model_prediction.Prediction import Prediction
import os

from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    is_uploaded = False
    try:
        pred_data_val = PredictionDataValidation()
        pred_data_val.deletePredictionFiles()
        pred_data_val.createPredictionFiles('Prediction_Files')
        #pred_data_val.createPredictionFiles('Prediction_Log')
        return render_template('index.html', is_uploaded = is_uploaded)
    except Exception as e:
        message = 'Error :: ' + str(e)
        return render_template('exception.html', exception=message)

@app.route('/uploader', methods=['GET','POST'])
def uploadFiles():
    try:
        if os.path.exists('Prediction_Files/Prediction.csv'):
            return redirect(url_for('home'))
        is_uploaded = False
        if request.method == 'POST':
            if request.files['file'] is not None:
                file = request.files['file']
                file.save(os.path.join('Prediction_Files/',secure_filename(file.filename)))
                is_uploaded = True

        return render_template('index.html', is_uploaded = is_uploaded)
    except Exception as e:
        message = 'Error :: ' + str(e)
        return render_template('exception.html', exception=message)


@app.route('/predict', methods=['GET'])
def predict():
    try:
        pred_val = PredictionValidation()
        pred_val.validation()

        pred = Prediction()
        pred.predict()

        return send_file(os.path.join('Prediction_Files/')+'Prediction.csv', as_attachment=True)
    except Exception as e:
        message = 'Error :: '+str(e)
        return render_template('exception.html', exception = message)


if __name__ == "__main__":
    app.run(debug=True)