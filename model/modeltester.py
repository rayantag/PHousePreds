import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from joblib import dump, load

scaler = load('/Users/rayant/app2/model/scaler.joblib')
# Load the saved model
loaded_model = load_model('med_model.h5')

# Prepare a new input for the model
new_input = [[25.0, 7.0, 7.0, 33]]  # replace with the actual averages for points, rebounds, and assists

# Don't forget to scale the new input with the same scaler used on the training data
new_input = scaler.transform(new_input)


# Use the model to make a prediction
prediction = loaded_model.predict(new_input)

print(f'Predicted points: {prediction[0][0]}')

