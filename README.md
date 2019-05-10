# BballGamePredictor
Final project for Databases class 2019 using Apache Hbase

## Required Dependencies 
In order to run our HBase basketball prediction script you must for have HBase installed. A tutorial for installing HBase can be found [here](http://hbase.apache.org/book.html#quickstart).

After installing HBase you must also install HappyBase, a Python API for interfacing with HBase and Python. That can be done with the following command:
`pip install happybase`

## Running `hbase_predictor.py`
Before a prediction calculation can be completed, a local instance of HBase must first be populated with game data found in the `2017-18_games.csv`. This can be completed by running the `populate_table` function. After the data has loaded into HBase, the prediction function, `run_calculator` can be ran with the required input variable.
