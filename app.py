import json
import requests
import sys
import os
from flask import Flask
from ruamel.yaml import YAML
from icalendar import Calendar, Event


yaml = YAML()
cal = Calendar()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
