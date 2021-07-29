from flask import Flask, request, render_template, Response
from predictionValidation import PredictionValidation
from prediction_data_validation.prediction_data_validation import PredictionDataValidation
from model_prediction.Prediction import Prediction
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/uploader', methods=['GET','POST'])
def uploadFiles():
    try:
        if request.method == 'POST':
            if request.files['file'] is not None:
                file = request.files['file']
                pred_data_val = PredictionDataValidation('Prediction_Files')
                pred_data_val.deletePredictionFiles()
                pred_data_val.createPredictionFiles()
                file.save(os.path.join('Prediction_Files/',secure_filename(file.filename)))
        return 'uploaded'
    except Exception as e:
        print(e)


@app.route('/predict', methods=['POST'])
def predictRouteClient():
    try:
        pred_val = PredictionValidation("path")
        pred_val.validation()

        pred = Prediction('')
        pred.predict()

        return Response("worked")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)