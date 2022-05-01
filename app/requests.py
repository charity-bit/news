from urllib import response
from app import app
import urllib.request
import json
from .models import article,source

Article = article.Article
Source = source.Source

BASE_SOURCE_URL = app.config['SOURCE_URL']
BASE_ARTICLES_URL = app.config['ARTICLES_URL']
GENERAL_URL = app.config['GENERAL_URL']
API_KEY = app.config['NEWS_API_KEY']



def get_sources():
    '''
    function to get the sources

    '''
    source_url = BASE_SOURCE_URL.format(API_KEY)
    with urllib.request.urlopen(source_url) as source_url:
        data = source_url.read()
        response = json.loads(data)
        print(response)

        results = None

        if response['sources']:
            sources_list = response['sources']
            results = process_source(sources_list)

        return results 



    
def process_source(response):
    sources_list = []
   
    for source in response:
        if source['url']:
                # (self,id,name,description,url,category,country):
            source_instance = Source(source['id'],source['name'],source['description'],source['url'],source['category'],source['country'])
            sources_list.append(source_instance)
    return sources_list

  
def get_source_articles(source_id):
    articles_base_url = BASE_ARTICLES_URL.format(source_id,API_KEY)
    with urllib.request.urlopen(articles_base_url) as articles_url:
        data = articles_url.read()
        response = json.loads(data)

        results  = None

        if response['articles']:
            articles_list = response['articles']
            results = process_articles(articles_list)

        return results

def get_articles(category):
    get_articles_url =  GENERAL_URL.format(category,API_KEY)
    with urllib.request.urlopen(get_articles_url) as articles_url:
        data = articles_url.read()
        response = json.loads(data)

        results  = None

        if response['articles']:
            articles_list = response['articles']
            results = process_articles(articles_list)

        return results
    



def process_articles(response):
    articles_results = []
    for article in response:
        if article['urlToImage']:
            # image,title,description,time,source_name,url,content)
            articles_instance = Article(article['urlToImage'],article['title'],article['description'],article['publishedAt'],article['source']['name'],article['url'])
            articles_results.append(articles_instance)

    return articles_results