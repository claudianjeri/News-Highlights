class Config:

    pass

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True #we set this to true so that we can run the application on debug mode. This will help with getting roors when they appear.
    