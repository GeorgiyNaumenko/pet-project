
import json
import requests
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from utils import DataLoader, Estimator 
from settings.constants import TRAIN_CSV, VAL_CSV, METRICS

# with open('settings/specifications.json') as f:
#     specifications = json.load(f)
    
# info = specifications['description']
# x_columns, y_column, metrics = info['X'], info['y'], info['metrics']

train_set = pd.read_csv(TRAIN_CSV, header=0)
val_set = pd.read_csv(VAL_CSV, header=0)

# train_x, train_y = train_set[x_columns], train_set[y_column]
# val_x, val_y = val_set[x_columns], val_set[y_column]

loader = DataLoader()
loader.fit(val_set)
val_processed, val_targets = loader.load_data()
print('data: ', val_processed[:10])

req_data = {'data': json.dumps(val_set.to_dict())}
response = requests.get('http://192.168.1.5:8000/predict', data=req_data)
api_predict = response.json()['prediction']
print('predict: ', api_predict[:10])

api_score = eval(METRICS[0])(val_targets, api_predict)
print('accuracy: ', api_score)