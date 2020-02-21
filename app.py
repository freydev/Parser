#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
from pathlib import Path

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'Server is running.'
    elif request.method == 'POST':
        data = request.files['avatar'].read()


report = 'Huy sosi guboy tryasi'

app.run(host='0.0.0.0', debug=True)

data = request.files['avatar'].read()
with open("test.wav", mode="wb") as new:
    new.write(data)
