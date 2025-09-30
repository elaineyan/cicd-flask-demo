from flask import Flask, jsonify
import os
import socket
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(host=socket.gethostname(), version=os.getenv("VERSION", "V1"))


@app.route("/health")
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
