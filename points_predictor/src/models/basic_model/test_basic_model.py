import pandas as pd
from tensorflow.keras.models import load_model
from preprocess import PreprocessBasicModel

"""
Testing the basic model.
"""
# Load the saved model
loaded_model = load_model('../../../models/basic_model.h5')

# Setting up test dataframe
test_input = [['yo', 25.0, 7.0, 7.0, 33]] 
test_df = pd.DataFrame(test_input, columns = ['Name', 'AVG_PTS', 'AVG_REB', 'AVG_AST', 'MIN'])

# Preprocess test data
preprocess = PreprocessBasicModel(test_df)
test_data = preprocess.getProcessedData()


# Use the model to make a prediction
prediction = loaded_model.predict(test_data)

print(f'Predicted points: {prediction[0][0]}')

