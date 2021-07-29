import os
import pickle

class FileHandler:
    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger = logger_object
        self.model_path = 'models/'

    def loadModel(self, filename):

        self.logger.log(self.file_object, 'Entered the loadModel method of FileHandler class')
        try:
            with open(self.model_path+filename+'.sav', 'rb') as f:
                self.logger.log(self.file_object, self.model_path.split('/')[1]+' loaded. Exiting loadModel method of FileHandler class')
                return pickle.load(f)

        except Exception as e:
            self.logger.log(self.file_object, 'Error occured in loadModel method of FileHandler class. Message: '+str(e))
            raise e
