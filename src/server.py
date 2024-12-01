from flask import Flask
from flask import request
from threading import Thread

import json, time, requests

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def main():
	return app.send_static_file('timer.html')

@app.route('/matchtimer')
def matchTimer():
	return app.send_static_file('matchTime.html')


if __name__ == '__main__':
	global matchTime
	global matchNum
	matchNum = 0
	matchTime = -1
	app.run(host="0.0.0.0", port=5002)
