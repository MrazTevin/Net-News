from flask import render_template
from app import app
from .request import get_sources


# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and
    its data
    '''

    # get general sources
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'Welcome to News Source'
    return render_template('index.html',title=title,business = business_sources,health=health_sources,science=science_sources,sports = sports_sources, technology = technology_sources,entertainment = entertainment_sources ,general=general_sources)


@app.route('/news/<int:news_id>')
def news(news_id):
    title = 'Read Articles from best Sources'
    return render_template('source.html', id=news_id, title=title)
