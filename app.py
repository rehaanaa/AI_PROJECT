# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Render!'
import os

port = int(os.environ.get('PORT', 10000))  # Default port is 10000
app.run(host='0.0.0.0', port=port)
