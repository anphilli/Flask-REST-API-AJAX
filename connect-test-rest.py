#!/usr/bin/env python

from flask import Flask, jsonify, render_template, Response
import capitals
import json

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/<name>', methods=['GET'])
def get_capital(name=''):

	print(name)
    # try:
    #     resp = jsonify(state=name, capital=capitals[name])
    # except KeyError:
    #     resp = jsonift(state=name, capital='not found')
	
	resp = jsonify(capital='Sacramento')
	return Response(resp.data, status=200, mimetype='application/json')


@app.route('/state', methods=['GET'])
def list_states():
    resp = jsonify(names=[state for state in capitals])
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='127.0.0.1', port=8081)

