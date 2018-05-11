from flask import Flask #import the Flask class from the flask module
from .main import views #import the views file.
from .config import DevConfig #import 

app = Flask(__name__)#This is initializing the application, creating an app instance, we pass in the name variable.

