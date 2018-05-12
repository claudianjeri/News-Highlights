from flask import Flask #import the Flask class from the flask module
# from .main import views #import the views file.
from .config import DevConfig #import config


app = Flask(__name__)#This is initializing the application, creating an app instance, we pass in the name variable.

# from .main import main as main_blueprint
# app.register_blueprint(main_blueprint)

app.config.from_object(DevConfig) #setting up config

from app import views