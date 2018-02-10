from app import app
import urllib.request,json
from .models import news

Source = news.Source

# getting apiKey
api_key = app.config['NEWS_API_KEY']

# getting news base url
base_url = app.config["NEWS_API_BASE_URL"]
