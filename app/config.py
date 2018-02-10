class Config:
    '''General Configuration Parent Class'''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'


class ProdConfig(Config):
    '''Production Configuration Child Class'''
    pass


class DevConfig(Config):
    '''Development Configuration Child Class'''
    DEBUG = True
