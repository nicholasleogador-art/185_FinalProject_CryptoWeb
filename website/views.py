from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/blog')
def blog():
    return render_template('blog.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/accounts')
def accounts_list():
    # Import here to avoid circular imports
    from .data import puzzles_db 
    return render_template('accounts_list.html', accounts=puzzles_db)