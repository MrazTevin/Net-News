from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# initializing application
app = Flask(__name__,instance_relative_config = True)

# configuration set up
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


# Initalizing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
