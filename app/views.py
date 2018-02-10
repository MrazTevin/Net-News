from flask import render_template
from app import app


# views
@app.route('/')
def index():
    message = 'Hello World'
    return render_template('index.html', message=message)


@app.route('/source<int:source_id>')
def source(source_id):
    return render_template('source.html', id=source_id)
