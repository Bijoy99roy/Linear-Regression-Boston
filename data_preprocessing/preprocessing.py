import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from file_operation.file_handler import FileHandler
class PreProcessing:
    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger = logger_object

    def isNullPresent(self, data):

        self.logger.log(self.file_object, 'Entered the isNullPresent method of PreProcessor class')
        self.has_null = False
        self.cols_with_missing_values = []
        self.cols = data.columns
        self.missing_value_count = []

        try:
            self.cols_with_missing_values = [i for i in self.cols if data[i].isnull().sum()>=1]
            self.missing_value_count = [data[i].isnull().sum() for i in self.cols_with_missing_values]
            if len(self.cols_with_missing_values) > 0:
                self.has_null = True
                self.dataframe_with_null = pd.DataFrame()
                self.dataframe_with_null['Columns'] = self.cols_with_missing_values
                self.dataframe_with_null['Missing value count'] = self.missing_value_count
                self.dataframe_with_null.to_csv('preprocessing_data/null_values.csv')
                self.logger.log(self.file_object, 'Found missing values. Data saved in null.value.csv.Exiting isNummPresent method of PreProcessor class')
            else:
                self.logger.log(self.file_object, 'No missing value found. Exiting isNummPresent method of PreProcessor class')
            return self.has_null, self.cols_with_missing_values
        except Exception as e:
            self.logger.log(self.file_object,
                                   'Exception occured in isNullPresent method of the PreProcessor class. Exception message:  ' + str(e))
            self.logger.log(self.file_object,
                                   'Finding missing values failed. Exited the isNullPresent method of the PreProcessor class')
            raise e

    def imputeMissingValues(self, data, cols_with_missing_values):

        self.logger.log(self.file_object, 'Entered imputeMissingValues method of PreProcessing class')
        self.data = data
        self.cols_with_missing_values = cols_with_missing_values
        try:

            self.imputer = FileHandler(self.file_object, self.logger).loadModel('simpleImputer')
            self.logger.log(self.file_object, 'Started imputing data.')
            #for i in self.cols_with_missing_values:

            self.data = pd.DataFrame(self.imputer.transform(self.data), columns=self.data.columns)
            self.logger.log(self.file_object, 'Imputing data complete!!. Exiting imputeMissingValues method of PreProcessing class')
            return self.data
        except ValueError:
            self.logger.log(self.file_object, 'Value Error occured in imputeMissingValues method of PreProcessing class. Message: '+ str(ValueError))
            self.logger.log(self.file_object, 'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
            raise ValueError
        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
            raise e


    def scaleFeatures(self, data):

        self.logger.log(self.file_object, 'Entered scaleFeature method of PreProcessing class')
        self.data = data
        try:

            self.scaler = StandardScaler()
            self.logger.log(self.file_object, 'Scaling the data starting')
            self.data = self.scaler.fit_transform((self.data))
            self.logger.log(self.file_object,'Data Scaling complete!!. Exiting scaleFeatures method of PreProcessing class')
            return self.data
        except Exception as e:
            self.logger.log(self.file_object, 'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger.log(self.file_object, 'Data Scaling failed. Exited the scaleFeatures method of the Preprocessor class')
            raise e









