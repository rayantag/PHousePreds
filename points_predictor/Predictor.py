from .src.models.basic_model.model import BasicModel
import os
import pandas as pd

MODELS = {
    "basic_model": BasicModel
}

class PointsPredictor():
    def __init__(self, model_name, modelParams):
        self.model = MODELS[model_name](modelParams)

    def train(self, verbose = False):
        self.model.train(verbose)

    def predict(self, player_id):
        currPath = os.path.dirname(__file__)
        fullDataPath = os.path.join(currPath, 'datasets/player_features.csv')
        full_data = pd.read_csv(os.path.normpath(fullDataPath))
        try:
            player_data = full_data[full_data['Player_ID'] == player_id].tail(1)
        except:
            return IndexError("Player data not there.")
        if player_data.size == 0:
            return IndexError("Player data not there.")
        return self.model.predict(player_data)