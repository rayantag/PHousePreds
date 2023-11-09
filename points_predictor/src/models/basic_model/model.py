from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import os
import pandas as pd
from .preprocess import PreprocessBasicModel
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

"""
Returns a fully connected neural network. 
Inputs:
    - num_layers: integer for how many layers you want
    - num_nodes: array where each ith element is the number of nodes in the i+1th layer
    - input_shape: tuple for shape of input
    - act_fns: array of activation functions for each layer

Returns:
Fully connected neural net with desired config
"""

class BasicModel():
    
    def __init__(self, params):
        try:
            currPath = os.path.dirname(__file__)
            modelPath = os.path.join(currPath, '../../../models/basic_model.h5')
            self.model = load_model(modelPath)
        except:
            num_layers = params["num_layers"]
            num_nodes = params["num_nodes"]
            input_shape = params["input_shape"]
            act_fns = params["act_fns"]
            layers = [Dense(num_nodes[0], activation = act_fns[0], input_shape = input_shape)]
            layers += [Dense(num_nodes[layer], activation = act_fns[layer]) for layer in range(1, num_layers - 1)]
            layers += [Dense(1)]
            self.model = Sequential(layers)

    def train(self, verbose = False):
        currPath = os.path.dirname(__file__)
        fullDataPath = os.path.join(currPath, '../../../datasets/player_features.csv')
        full_data = pd.read_csv(os.path.normpath(fullDataPath))

        preprocesser = PreprocessBasicModel(full_data)
        train_data, test_data, train_labels, test_labels = preprocesser.getProcessedDataTraining()   

        if verbose: self.model.summary()

        self.model.compile(optimizer = 'adam', loss = 'mse', metrics = ['mae'])
        history = self.model.fit(train_data, train_labels, epochs=10, validation_split=0.2)
        loss, mae = self.model.evaluate(test_data, test_labels)
        preprocesser.done()

        if verbose: 
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
        self.model.save(os.path.normpath(modelPath))
    
    def predict(self, data, verbose = False):
        preprocess = PreprocessBasicModel(data)
        test_data = preprocess.getProcessedData()
        prediction = self.model.predict(test_data)

        if verbose: print(f'Predicted points: {prediction[0][0]}')

        return prediction[0][0]