# from .Predictor import PointsPredictor
# import os
# import pandas as pd


# predictor = PointsPredictor("basic_model", 
#                             {
#                                 "num_layers": 4,                     # number of layers
#                                 "num_nodes": [150, 50, 8, 1],        # number of nodes in each layer 
#                                 "input_shape": (4,),                 # input shape
#                                 "act_fns": ['relu', 'relu', 'relu']  # activation functions -- only 2 as first and last layer dont have
#                             }
#                         )

# currPath = os.path.dirname(__file__)
# fullDataPath = os.path.join(currPath, '../../datasets/raw_data.csv')
# full_data = pd.read_csv(os.path.normpath(fullDataPath))

# player_ids = full_data["Player_id"].unique()

# for id in player_ids:
    