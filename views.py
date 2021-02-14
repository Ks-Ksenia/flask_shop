from app import app, db
from flask import render_template, redirect, request, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user

from models import User, Product
from forms import LoginForm, RegistrationForm


@app.route('/')
def index():
    return redirect(url_for('menu.catalog'))


@app.route('/search/')
def search():
    q = request.args.get('q')
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages, products = [], []

    if q:
        products = Product.query.filter(Product.product_name.contains(q)|Product.product_name.contains(q))
        pages = products.paginate(page=page, per_page=1)

    return render_template('search.html', products=products, pages=pages, q=q)


@app.login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if not current_user.is_authenticated:

        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()

            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember.data)

                return redirect(request.args.get('next') or url_for('index'))
            else:
                flash('Неверный email или пароль')

        return render_template('login.html', form=form, title="Вход")
    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password1.data)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('login'))
        else:
            flash('Пользователь с таким email уже существует')

    return render_template('singup.html', form=form, title='Регистрация')




