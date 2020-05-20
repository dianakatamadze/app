from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
     user = {'username': 'дорогой клиент'}
     name = {'shopname': 'Dolce Vita'}
     return render_template('index.html',title='Главная',user=user,name=name)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Покупка', form=form)
@app.route('/shop_all')
def shop_all():
    return render_template('shop_all.html',title='Все товары')
@app.route('/shop_cross')
def shop_cross():
    return render_template('shop_cross.html',title='Cумки через плечо')
@app.route('/shop_bag')
def shop_bag():
    return render_template('shop_bag.html',title='Большие сумки')
@app.route('/contacts')
def contacts():
    return render_template('contacts.html',title='Контакты')
@app.route('/suns')
def suns():
    return render_template('suns.html',title='Sunset')
    