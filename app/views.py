from flask import render_template
from app import app


# views
@app.route('/')
def index():
    title = 'Welcome to News Source'
    return render_template('index.html', title=title)


@app.route('/source/<int:source_id>')
def source(source_id):
    title = 'Read Articles from best Sources'
    return render_template('source.html', id=source_id, title=title)
