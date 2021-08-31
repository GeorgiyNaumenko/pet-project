import os
from sklearn.svm import SVC

DATA_FOLDER = 'C:\\Users\\gogan\\source\\repos\\pet-project\\pet-project\\data'
TRAIN_CSV = os.path.join(DATA_FOLDER, 'train.csv')
VAL_CSV = os.path.join(DATA_FOLDER, 'val.csv')
MODELS_FOLDER = 'C:\\Users\\gogan\\source\\repos\\pet-project\\pet-project\\models'
MODELS = {'model1': SVC(kernel='linear', C=0.5)}
SAVED_ESTIMATORS = {'model1': os.path.join(MODELS_FOLDER, 'SVC.pickle')}
METRICS = ['accuracy_score']