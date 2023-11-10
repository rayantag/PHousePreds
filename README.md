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
$ python -m back.server
```

Then, open a new terminal session and run the following commands from the `PHousePreds` directory:
```
$ source PinkHousePredictions/bin/activate
$ cd src
$ npm start
```

## Possible Issues
When you run `npm start` in PHousePreds/src, if you get an error saying
```
Module not found: Error: Can't resolve '@fortawesome/react-fontawesome'
```
or any similar error relating to not being able to resolve `'@fortawesome/...'`, run the following command:
```
npm i --save @fortawesome/react-fontawesome
```
and then run `npm start` again.
