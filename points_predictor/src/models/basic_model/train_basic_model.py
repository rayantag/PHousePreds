import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump, load
from preprocess import PreprocessBasicModel
from model import BasicModel
import os

"""
Training script for basic model.
So far it allows you to train by running from command line.

TDOD:
Implement trainBasicModel method which will allow you to train by importing this package somewhere else.
"""

currPath = os.path.dirname(__file__)
fullDataPath = os.path.join(currPath, '../../../datasets/player_features.csv')
full_data = pd.read_csv(os.path.normpath(fullDataPath))

preprocesser = PreprocessBasicModel(full_data)
train_data, test_data, train_labels, test_labels = preprocesser.getProcessedDataTraining()

basic_model = BasicModel(
                            4,                # number of layers
                            [150, 50, 8, 1],  # number of nodes in each layer 
                            (4,),             # input shape
                            ['relu', 'relu', 'relu']  # activation functions -- only 2 as first and last layer dont have
                        )

if __name__ == "__main__":
    basic_model.summary()

    basic_model.compile(optimizer = 'adam', loss = 'mse', metrics = ['mae'])
    history = basic_model.fit(train_data, train_labels, epochs=10, validation_split=0.2)
    loss, mae = basic_model.evaluate(test_data, test_labels)
    preprocesser.done()

    print(f'Test Mean Absolute Error: {mae}')
    plt.figure(figsize=(12, 6))
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper right')
    plt.show()

    modelPath = os.path.join(currPath, '../../../models/basic_model.h5')
    basic_model.save(os.path.normpath(modelPath))