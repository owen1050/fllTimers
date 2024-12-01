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


#api endpoints
@app.route('/api/getMatchTime')
def apiGetMatchTime():
	global matchTime
	print(matchTime)
	if(matchTime == -1):
		return str(-1)
	r = time.time() - matchTime
	print(r)
	return str(int(r))

@app.route('/api/resetMatchTime')
def apiResetMatchTime():
	global matchTime
	matchTime = -1
	return str(0)

@app.route('/api/startMatch')
def apiStartMatch():
	global matchTime
	matchTime  = time.time()
	print(matchTime)
	return str(0)


@app.route('/api/endMatch')
def apiEndMatch():
	global matchTime
	matchTime = -1
	return str(0)


@app.route('/api/addOneMatchNum')
def apiAddOneMatchNum():
	global matchNum
	matchNum = matchNum + 1
	return str(0)

@app.route('/api/subOneMatchNum')
def apiSubOneMatchNum():
	global matchNum
	matchNum = matchNum - 1
	return str(0)

@app.route('/api/getMatchNum')
def apiGetMatchNum():
	global matchNum
	return str(matchNum)



if __name__ == '__main__':
	global matchTime
	global matchNum
	matchNum = 0
	matchTime = -1
	app.run(host="0.0.0.0", port=5002)
