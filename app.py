from flask import Flask, jsonify
import pandas as pd

songs = pd.read_csv('songs.csv')


app = Flask(__name__)

@app.route('/songs')
def index():
	return jsonify(list(songs['title']))

@app.route('/ping')
def ping():
	return 'pong :)))'

@app.route('/artist/<string:anArtist>')
def getSongsFrom(anArtist):
	return jsonify(list(songs[songs['artist'] == anArtist]['title']))

@app.route('/song/<string:aSongTitle>')
def getDescriptionOf(aSongTitle):
	return jsonify(list(songs[songs['title'] == aSongTitle]['description']))
