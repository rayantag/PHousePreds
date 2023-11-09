from points_predictor.Predictor import PointsPredictor
from flask import Flask, request
from flask_cors import CORS, cross_origin
from joblib import dump, load
import numpy as np
from tensorflow.keras.models import load_model
from nba_api.stats.static import players
from nba_api.stats.endpoints import playerindex
from rapidfuzz import fuzz, process
import pandas as pd

app = Flask(__name__)
app.debug = True

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

actives = players.get_active_players()
name_list = [active_player['full_name'] for active_player in actives]

@app.route("/convert", methods=['POST'])
@cross_origin()
def nameToNumber():
    try:
        input_name = request.get_json().get('inputArray')
        plays = players.find_players_by_full_name(input_name)
        if not plays:
          selected = process.extractOne(input_name, name_list, scorer=fuzz.WRatio)
          return {"message": f'Did you mean to specify "{selected[0]}"?', "id": -1}, 400
        if (len(plays) > 1):
            return {"message": "Please be more specific!", "id": 0}, 400
        play_id = plays[0]['id']
        p = playerindex.PlayerIndex(season="2023-24")
        p_df = p.get_data_frames()[0]
        player_row = p_df[p_df['PERSON_ID'] == play_id]
        if player_row.empty:
            return {"message": "Please input a different name!", "id": 0}, 400
        predictor = PointsPredictor("basic_model", 
                            {
                                "num_layers": 4,                     # number of layers
                                "num_nodes": [150, 50, 8, 1],        # number of nodes in each layer 
                                "input_shape": (4,),                 # input shape
                                "act_fns": ['relu', 'relu', 'relu']  # activation functions -- only 2 as first and last layer dont have
                            }
                        )
        pred = predictor.predict(play_id)

        return {"message": str(pred), "id": play_id}, 200
    except Exception as e:
        print(e)
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(port=5000)  # run the server on port 5000