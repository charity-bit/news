import imp
from flask import render_template
from app import app
from .requests import get_sources


@app.route('/')
def index():
    sources = get_sources()
    return render_template('index.html',sources = sources)