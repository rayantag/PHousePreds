from flask import Flask, request
from flask_cors import CORS, cross_origin
from joblib import dump, load
import numpy as np
from tensorflow.keras.models import load_model
from nba_api.stats.static import players
from nba_api.stats.endpoints import playerindex
from rapidfuzz import fuzz, process

app = Flask(__name__)
app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = load_model('/Users/rayant/app2/model/med_model.h5')
scaler = load('/Users/rayant/app2/model/scaler.joblib')

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
          return {"message": f'Did you mean to specify "{selected[0]}"?'}, 400
        play_id = plays[0]['id']
        p = playerindex.PlayerIndex(season="2022-23")
        p_df = p.get_data_frames()[0]
        player_row = p_df[p_df['PERSON_ID'] == play_id]
        vals = [player_row['PTS'].values[0], player_row['REB'].values[0], player_row['AST'].values[0], 33]
        model_input = np.array(vals).reshape(1, -1)
        model_input = scaler.transform(model_input)
        pred = model.predict(model_input)
        return {"message": str(pred[0][0])}, 200
    except Exception as e:
        print(e)
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(port=5000)  # run the server on port 5000