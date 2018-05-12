from app import app#importing the app module
import urllib.request, json #this will help in the creation to our API URL and send it to json modules. 
from .models import news

News = news.News
api_key = app.config['NEWS_API_KEY']
#getting the api key for requests.

base_url = app.config ["NEWS_API_BASE_URL"]#this how config objects are created.





