from .Predictor import PointsPredictor
from .src.data.create_player_features import getAveragePlayerStats
from .src.data.data_collect import collectAllPlayerData

"""
First we have to collect the data and extract relavent features.


Hardcoded for now but model name and params will be retrieved from json that is passed in.
"""

model_name = "basic_model"

model_params = {
                    "num_layers": 4,                     # number of layers
                    "num_nodes": [150, 50, 8, 1],        # number of nodes in each layer 
                    "input_shape": (4,),                 # input shape
                    "act_fns": ['relu', 'relu', 'relu']  # activation functions -- only 2 as first and last layer dont have
                }

predictor = PointsPredictor(model_name, model_params)
predictor.train(True)