class Config:
    
    NEWS_API_KEY = '8a48624dfbfc41d8a7009f960cccd473'
    NEWS_BASE_URL =' https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_NEWS_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True #we set this to true so that we can run the application on debug mode. This will help with getting roors when they appear.
    
    NEWS_API_KEY = '8a48624dfbfc41d8a7009f960cccd473' 

    # config_options = {
    #     'development' :DevConfig
    #     'production' : ProdConfig
    # }