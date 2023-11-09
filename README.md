# PinkHousePredictions
An ML powered app that predicts how many points a given NBA player will score in their next game.

## Setup
Run the following commands
```
$ git clone https://github.com/rayantag/PHousePreds.git
$ cd PHousePreds
$ pip install virtualenv # if you dont have vitualenv installed
$ python -m venv PinkHousePredictions
$ source PinkHousePredictions/bin/activate
$ pip install -r requirements.txt
```

## How to run
Run the following command from the PHousePreds directory:
```
python -m back.server
```

Then, open a new terminal session and run the following command from `PHousePreds/src`:
```
npm start
```