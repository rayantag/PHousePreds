from .src.models.basic_model.model import BasicModel
import os
import pandas as pd

MODELS = {
    "basic_model": BasicModel
}

class PointsPredictor():
    def __init__(self, model_name, modelParams):
        self.model = MODELS[model_name](modelParams)

    def predict(self, player_id):
        currPath = os.path.dirname(__file__)
        fullDataPath = os.path.join(currPath, 'datasets/player_features.csv')
        full_data = pd.read_csv(os.path.normpath(fullDataPath))
        player_data = full_data[full_data['Player_ID'] == player_id].tail(1)
        return self.model.predict(player_data)