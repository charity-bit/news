
from flask import render_template
from . import main
from ..requests import get_sources,get_source_articles,get_articles


@main.route('/')
def index():
    sources = get_sources()
    title = '1NEWS'
    return render_template('index.html',sources = sources,title=title)


@main.route('/articles/<source_id>')
def articles(source_id):
    title = 'Articles'
    articles = get_source_articles(source_id)
    return render_template('articles.html',articles = articles,title = title)

@main.route('/sports')
def sports():
    title = 'Sports'
    articles = get_articles('sports')
    return render_template('sports.html',articles = articles,title = title)

@main.route('/business')
def politics():
    title ='Business'
    articles = get_articles('business')
    return render_template('business.html',articles = articles,title = title)

@main.route('/technology')
def tech():
    title = 'Technology'
    articles = get_articles('technology')
    return render_template('technology.html',articles = articles,title = title)

@main.route('/entertainment')
def entertainment():
    title = 'Entertainment'
    articles = get_articles('entertainment')
    return render_template('entertainment.html',articles = articles,title = title)

@main.route('/health')
def health():
    title = 'Health'
    articles = get_articles('health')
    return render_template('health.html',articles = articles,title = title)





