class Config:
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    # https://newsapi.org/v2/top-headlines?country=us&category=sports
    GENERAL_URL = 'https://newsapi.org/v2/top-headlines?language=en&category={}&apiKey={}'
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
  

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True