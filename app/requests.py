from app import app#importing the app module
import urllib.request, json #this will help in the creation to our API URL and send it to json modules. 
from .models import news

News = news.News
api_key = app.config['NEWS_API_KEY']
#getting the api key for requests.

base_url = app.config ["NEWS_API_BASE_URL"]#this how config objects are created.

def get_news(category): #a function that takes news category as an argument
    get_news_url = base_url.format(category, api_key) #

    with urllib.request.urlopen(get_news_url) as url: #this sends the request as a url
        get_news_data =url.read()#reads the response then stores it in the get_news_data
        get_news_response = json.loads(get_news_data)#json response i.e the get_news_data is then converted to a python dictionary

        news_results = None

        if get_news_response['sources']: #checks if the response has any results. 
            news_results_list = get_news_response['sources']#if there is results then 
            news_results = process_results(news_results_list)

    return news_results



