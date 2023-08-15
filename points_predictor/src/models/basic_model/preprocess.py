import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from joblib import dump, load
import os

"""
This class is what will do the feature selection for the basic model.

Instantiate by passing in full data as a dataframe : preprocess = PreprocessBasicModel(data)
Then, get the processed data by calling getProcessedData: processedData = preprocess.getProcessedData()
"""

class PreprocessBasicModel:
    def __init__(self, data):
        self.full_data = data
        self.scalerPath = os.path.join(os.path.dirname(__file__), 'scaler.joblib')
        try:
            self.scaler = load(self.scalerPath)
        except OSError:
            self.scaler = StandardScaler()

    def getProcessedData(self):
        features = self.full_data[['AVG_PTS', 'AVG_REB', 'AVG_AST', 'MIN']].values
        return self.scaler.transform(features)    

    def getProcessedDataTraining(self, test_size = 0.2, random_state = 81):
        features = self.full_data[['AVG_PTS', 'AVG_REB', 'AVG_AST', 'MIN']].values
        labels = self.full_data['PTS'].values
        train_data, test_data, train_labels, test_labels = train_test_split(features, 
                                                            labels, 
                                                            test_size = test_size, 
                                                            random_state = random_state)
        train_data = self.scaler.fit_transform(train_data)
        test_data = self.scaler.transform(test_data)
        return train_data, test_data, train_labels, test_labels

    
    def done(self):
        dump(self.scaler, self.scalerPath) 
