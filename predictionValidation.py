import os
from application_logging.logger import App_Logger
from prediction_data_validation.prediction_data_validation import PredictionDataValidation

class PredictionValidation:
    def __init__(self, path):
        self.file = path
        self.raw_data = PredictionDataValidation(path)
        self.logger = App_Logger()

    def validation(self):
        try:
            f = open("Prediction_Log/Prediction_Log.txt", "a+")

            self.logger.log(f,"Validation started for Prediction Data")
            columnNumber, columnNames, requiredColumns = self.raw_data.getSchemaValues()
            #validating columns length
            self.logger.log(f, "Starting columns length validation")
            self.raw_data.validateColumnLength(columnNumber)
            self.logger.log(f, "Columns length validation complete!!")



        except Exception as e:
            print(e)
        f.close()

