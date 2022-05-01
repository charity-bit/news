from urllib import response
from app import app
import urllib.request
import json
from .models import article,source

Article = article.Article
Source = source.Source

BASE_SOURCE_URL = app.config['SOURCE_URL']
BASE_ARTICLES_URL = app.config['ARTICLES_URL']
API_KEY = app.config['NEWS_API_KEY']

def get_sources():
    source_url = BASE_SOURCE_URL.format(API_KEY)
    with urllib.request.urlopen(source_url) as source:
        data = source.read()
        response = json.loads(data)
        print(response)

        results = None

        if response['sources']:
            sources_list = response['sources']
            results = process_response(sources_list)

        return results 



    
def process_response(response):
    list = []
   
    for source in response:
        if source['url']:
                # (self,id,name,description,url,category,country):
            source_instance = Source(source['id'],source['name'],source['description'],source['url'],source['category'],source['country'])
            list.append(source_instance)
    return list

  




def get_source_articles(source_id):
    pass


def get_articles():
    pass