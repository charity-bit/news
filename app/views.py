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

@app.route('/business')
def politics():
    articles = get_articles('business')
    return render_template('business.html',articles = articles)

@app.route('/technology')
def tech():
    articles = get_articles('technology')
    return render_template('technology.html',articles = articles)

@app.route('/entertainment')
def entertainment():
    articles = get_articles('entertainment')
    return render_template('entertainment.html',articles = articles)

@app.route('/health')
def health():
    articles = get_articles('health')
    return render_template('health.html',articles = articles)





