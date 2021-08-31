import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

class DataLoader(object):

    def fit(self, dataset):
        self.dataset = dataset.copy()
        self.target = self.dataset['Drug']
        self.dataset = self.dataset.drop('Drug', axis=1)

    def load_data(self):

        # encode target value
        self.target_encoder = LabelEncoder()
        self.target_encoder.fit(self.target)
        self.target = self.target_encoder.transform(self.target)

        # add categorical age, replace with age
        self.dataset['Age'] = pd.qcut(self.dataset['Age'], 4)

        # encode categorical age
        self.age_encoder = LabelEncoder()
        self.age_encoder.fit(self.dataset['Age'])
        self.dataset['Age'] = self.age_encoder.transform(self.dataset['Age'])

        # add Na_to_K categorical
        self.dataset['Na_to_K_categorical'] = pd.cut(self.dataset['Na_to_K'], 2)

        # encode Na_to_K categorical
        self.natok_encoder = LabelEncoder()
        self.natok_encoder.fit(self.dataset['Na_to_K_categorical'])
        self.dataset['Na_to_K_categorical'] = self.natok_encoder.transform(self.dataset['Na_to_K_categorical'])

        # encode sex
        self.sex_encoder = LabelEncoder()
        self.sex_encoder.fit(self.dataset['Sex'])
        self.dataset['Sex'] = self.sex_encoder.transform(self.dataset['Sex'])

        # encode BP
        self.bp_encoder = LabelEncoder()
        self.bp_encoder.fit(self.dataset['BP'])
        self.dataset['BP'] = self.bp_encoder.transform(self.dataset['BP'])

        # encode Cholesterol
        self.cholesterol_encoder = LabelEncoder()
        self.cholesterol_encoder.fit(self.dataset['Cholesterol'])
        self.dataset['Cholesterol'] = self.cholesterol_encoder.transform(self.dataset['Cholesterol'])

        try:
            return self.dataset.drop('Unnamed: 0', axis=1), self.target
        except:
            return self.dataset, self.target

