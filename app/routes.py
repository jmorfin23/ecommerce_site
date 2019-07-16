from app import app

from flask import render_template




@app.route('/')
@app.route('/index')
def index():
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

    return render_template('index.html', products = products, title='Home')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route('/title')
def title():
    return render_template('form.html', title='Change Title')
