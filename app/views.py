from flask import render_template#import the render_template function from flask
# from . import main#import the app instance from the app folder
from app import app
from .requests import get_news

@app.route('/')
def index():
    

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')#the imported function takes the name of the template as its first argument.

@app.route('/')
def news(news_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html')

@app.route('/')
def index():
    
    

