import imp
from flask import render_template
from app import app
from .requests import get_sources,get_source_articles,get_articles


@app.route('/')
def index():
    sources = get_sources()
    return render_template('index.html',sources = sources)


@app.route('/articles/<source_id>')
def articles(source_id):
     articles = get_source_articles(source_id)
     return render_template('articles.html',articles = articles)

@app.route('/sports')
def sports():
    articles = get_articles('sports')
    return render_template('sports.html',articles = articles)

@app.route('/politics')


