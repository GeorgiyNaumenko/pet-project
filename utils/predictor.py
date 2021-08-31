import pickle

from settings.constants import SAVED_ESTIMATORS


class Predictor:
    def __init__(self, model_name):
        self.loaded_estimator = pickle.load(open(SAVED_ESTIMATORS[model_name], 'rb'))

    def predict(self, data):
        return self.loaded_estimator.predict(data)
