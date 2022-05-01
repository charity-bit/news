class Config:
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ALL_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    EVERYTHING = ''

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True