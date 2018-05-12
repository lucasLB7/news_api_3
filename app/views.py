from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():
    title = 'SPY-WITNESS NEWS -- HOME'
    return render_template('index.html', title = title)

@app.route('/register')
def register():
    title = 'SPY-WITNESS NEWS -- HOME'



@app.route('/news')
def news():
    business_articles = get_news("business")
    title = 'WORLD OVERVIEW - Spy-Witness news'
    return render_template('index.html',title = title, business_articles = business_articles)
