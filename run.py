# -*- encoding: utf-8 -*-
"""
Alex Little 2021
"""

from flask import Flask, render_template


app = Flask(__name__, template_folder='./apps/templates')


@app.route('/')
def index():
    return render_template('index.html', segment='index')


@app.route('/page1')
def page1():
    return "Booo!"



if __name__ == "__main__":
    app.run()
