from app import app

from flask import render_template, url_for, redirect
from app.forms import TitleForm, ContactForm, LoginForm, RegisterForm, PostForm



@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
def index(header=''):
    products = [
    {
        'id': 1001,
        'title': 'soap',
        'price': '3.98',
        'desc': 'Very clean soap'

    },
    {
        'id': 1002,
        'title': 'apples',
        'price': '2.98',
        'desc': 'granny smith'

    },
    {
        'id': 1003,
        'title': 'dishwasher',
        'price': '3980.00',
        'desc': 'cleans very dirty dishes'

    },
    {
        'id': 1004,
        'title': 'carrots',
        'price': '1.50',
        'desc': 'great for rabbits'

    }
    ]

    return render_template('index.html', products = products, title='Home', header=header)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route('/title', methods=['GET', 'POST'])
def title():
    #create an instance of the form
    form = TitleForm()

    #write a conditional that checks if form was submitted properly, then do something with the Data
    if form.validate_on_submit():

        return redirect(url_for('index', header=form.title.data))
        # print(f'{form.title.data}') #name of form.nameofinput.data
    return render_template('form.html', form = form , title='Change Title')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        #TODO: setup code
        password
    return render_template('form.html', form=form, title='Login')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        #TODO: setup code
        password
    return render_template('form.html', form=form, title='Register')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        #TODO: setup code
        password
    return render_template('form.html', form=form, title='Contact Us')
#temporary variable for testing, generally don't declare variables there
posts = [
    {
        'post_id': 1,
        'tweet': 'My favorite suit is spades.',
        'date_posted': '7/17/2019'
    },

    {
        'post_id': 2,
        'tweet': 'I like Boston',
        'date_posted': '7/18/2019'
    },

    {
        'post_id': 3,
        'tweet': 'My cat got sprayed by a skunk',
        'date_posted': '7/19/2019'
    }
]
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = PostForm()

    if form.validate_on_submit():
        posts.append(
        {
            'post_id': len(posts) + 1,
            'tweet': form.tweet.data,
            'date_posted': 7/17/2019

        }
        )
        print(form.tweet.data)
        return redirect(url_for('profile'))

    return render_template('profile.html', title='Profile', form=form, posts=posts)
