#!/usr/bin/env python3
import os

from flask import Flask, render_template, request

__version__ = '0.1.0'

# From "application factories", https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    return app

print("\nNOTE: On mac, ignore what Flask tells you: Press Ctrl-\ (not Ctrl-C) to quit!\n")

app = create_app()

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # set hostname to '0.0.0.0' instead of 'localhost' to bind to all interfaces
    hostname = os.environ.get('HOSTNAME', 'localhost')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=hostname, port=port)
