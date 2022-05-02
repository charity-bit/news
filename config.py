import os

class Config:
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    GENERAL_URL = 'https://newsapi.org/v2/top-headlines?language=en&category={}&apiKey={}'
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

  

class ProdConfig(Config):
    pass


class DevConfig(Config):
DEBUG = True


config_options = {
    'development':DevConfig,
    'production': ProdConfig
}