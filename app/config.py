class Config:
    '''General Configuration Parent Class'''
    pass


class ProdConfig(Config):
    '''Production Configuration Child Class'''
    pass


class DevConfig(Config):
    '''Development Configuration Child Class'''
    DEBUG = True
