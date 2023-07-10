from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog, leaguedashptteamdefend, boxscoredefensive, leaguegamefinder, boxscorematchups
from nba_api.stats.endpoints import defensehub, draftboard, drafthistory, playerawards, playercareerstats, gamerotation
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

bron_df = pd.read_csv('med_data.csv')

# Construct features and labels. TODO --> PROJECTED MINUTES, OPPOSING DEFENSE, AGE
features = bron_df[['AVG_PTS', 'AVG_REB', 'AVG_AST', 'MIN']].values
labels = bron_df['PTS'].values

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=81)

# Normalize the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

lebron_pred = Sequential([
    Dense(150, input_shape = (4,)),
    Dense(50, activation = 'relu'),
    Dense(8, activation = 'relu'),
    Dense(1)
])

lebron_pred.summary()

lebron_pred.compile(optimizer = 'adam', loss = 'mse', metrics = ['mae'])
history = lebron_pred.fit(X_train, y_train, epochs=10, validation_split=0.2)
loss, mae = lebron_pred.evaluate(X_test, y_test)

print(f'Test Mean Absolute Error: {mae}')
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()

lebron_pred.save('med_model.h5')
dump(scaler, 'scaler.joblib') 

# # Load the saved model
# loaded_model = load_model('med_model.h5')

# # Prepare a new input for the model
# new_input = [[25.0, 7.0, 7.0, 30]]  # replace with the actual averages for points, rebounds, and assists

# # Don't forget to scale the new input with the same scaler used on the training data
# new_input = scaler.transform(new_input)

# # Use the model to make a prediction
# prediction = loaded_model.predict(new_input)

# print(f'Predicted points: {prediction[0][0]}')

