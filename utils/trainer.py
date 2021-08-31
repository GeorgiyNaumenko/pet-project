from sklearn.svm import SVC
from settings.constants import MODELS


class Estimator:
    @staticmethod
    def fit(train_x, train_y, model_name):
        return MODELS[model_name].fit(train_x, train_y)

    @staticmethod
    def predict(trained, test_x):
        return trained.predict(test_x)
