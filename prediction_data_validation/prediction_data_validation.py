from application_logging.logger import App_Logger
import json
import os
import shutil
import pandas as pd

class PredictionDataValidation:
    def __init__(self, file_path):
        self.path = file_path
        self.logger = App_Logger()
        self.schema = 'Prediction_Schema.json'

    def deletePredictionFiles(self):
        try:
            shutil.rmtree('Prediction_Files/')
        except Exception as e:
            pass
    def createPredictionFiles(self):
        try:
            os.mkdir('Prediction_Files/')
        except Exception as e:
            pass
    def getSchemaValues(self):

        try:
            with open(self.schema, 'r') as f:
                dic = json.load(f)
                f.close()
            columnNames = dic["columnNames"]
            columnNumber = dic["columnNumber"]
            requiredColumns = dic["requiredColumns"]
            file = open("Prediction_Log/valuesFromSchemaLog.txt",'a+')
            message = "ColumnNumber: "+str(columnNumber)+"\t"+"RequiredColumns: "+str(requiredColumns)+"\n"
            self.logger.log(file,message)

            file.close()

        except ValueError:
            file = open("Prediction_Log/valuesFromSchemaLog.txt", 'a+')
            message = "ValueError:Value not found inside Schema_prediction.json"
            self.logger.log(file, message)

            file.close()

        except KeyError:
            file = open("Prediction_Log/valuesFromSchemaLog.txt", 'a+')
            message = "KeyError:key value error incorrect key passed"
            self.logger.log(file, message)

            file.close()
            raise KeyError
        except Exception as e:
            file = open("Prediction_Log/valuesFromSchemaLog.txt", 'a+')
            self.logger.log(file, str(e))
            file.close()
            raise  e

        return columnNumber, columnNames, requiredColumns

    def validateColumnLength(self, columnNumber):

        try:
            f = open("Prediction_Log/columnValidationLog.txt", 'a+')
            self.logger.log(f, "Column Length Validation Started!!")
            for file in os.listdir('Prediction_Files/'):
                csv = pd.read_csv('Prediction_Files/'+file)
                if csv.shape[1] == columnNumber:
                    pass
                else:
                    self.logger.log(f, "Invalid column length for the file!! Exiting...")
                    raise Exception("Invalid column length for the file!!")
            self.logger.log(f, "Columns length validation complete!!")
        except Exception as e:
            f = open("Prediction_Log/columnValidationLog.txt", 'a+')
            self.logger.log(f, str(e))
            f.close()
            raise e
        f.close()

    def getRequiredColumns(self, requiredColumns):

        try:
            columns = None
            f = open("Prediction_Log/RequiredColumnsLog.txt", 'a+')
            self.logger.log(f, "Getting required columns...")
            for file in os.listdir('Prediction_Files/'):
                csv = pd.read_csv('Prediction_Files/'+file)
                columns = csv[requiredColumns].copy()
                self.logger.log(f,'Columns aquired from '+file)
        except Exception as e:
            self.logger.log(f, 'Exception occured in getRequiredColumns method in PredictionDataValidation class. Message: '+str(e))
            f.close()
            raise Exception()
        f.close()
        return columns





