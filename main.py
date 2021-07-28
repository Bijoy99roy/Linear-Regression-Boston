from flask import Flask, request, render_template, Response
from predictionValidation import PredictionValidation
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predictRouteClient():
    try:
        pred = PredictionValidation("path")
        pred.validation()
        return Response("worked")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)