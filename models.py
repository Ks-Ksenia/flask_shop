from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager #, UserMixin
from flask_security import RoleMixin, UserMixin


roles_users = db.Table('roles_users',
           db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
           db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
           )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    is_superuser = db.Column(db.Boolean(), default=False)
    created = db.Column(db.String(), default=datetime.now)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    customer = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return f'Пользователь {self.username} с почтой: {self.email}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))


class MainMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(100), unique=True)
    img = db.Column(db.String(500))
    submenu = db.relationship('Submenu', backref='submenu', lazy='dynamic')

    def __repr__(self):
        return self.title


class Submenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(100), unique=True)
    img = db.Column(db.String(500))
    main_menu_id = db.Column(db.Integer, db.ForeignKey('main_menu.id'))
    product = db.relationship('Product', backref='submenu')

    def __repr__(self):
        return self.title




class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='user_customer', uselist=False)
    cart = db.Column(db.Integer, db.ForeignKey('cart.id', ondelete='CASCADE'))
    order = db.relationship('Order', backref='order_customer')

    def __repr__(self):
        return str(self.user)

cart_products = db.Table('cart_products',
                db.Column('cart_id', db.Integer, db.ForeignKey('cart.id')),
                db.Column('cart_product_id', db.Integer, db.ForeignKey('cart_product.id')))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.relationship('Customer', backref='cart_customer', uselist=False)
    # products = db.relatinship('Product', secondary=cart_product, backref='product', )
    total_products = db.Column(db.Integer())
    final_price = db.Column(db.Integer())
    order = db.relationship('Order', backref='order_cart')

    def __repr__(self):
        return f'{self.customer}  с коризиной: {self.id}'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column('url', db.String(100), unique=True)
    img = db.Column('Картинка', db.String(200))
    price = db.Column('Цена', db.Integer())
    description = db.Column('Описание', db.Text)
    collection = db.Column('Коллекция товара', db.Integer, db.ForeignKey('submenu.id'))
    product_name = db.Column(db.String(200))
    code_product = db.Column('Код товара', db.String(20), unique=True)
    article = db.Column('Артикул', db.String(20), unique=True)
    type = db.Column('Тип', db.String(100))
    sex = db.Column('Пол', db.String(50))
    country = db.Column('Страна', db.String(50))
    material = db.Column('Материал', db.String(100))
    age = db.Column('Возраст', db.String(10))
    availability = db.Column('Наличие', db.String(10))
    review = db.Column(db.Integer(), default=0)        # пока под вопросом
    cart_product = db.relationship('CartProduct', backref='cartproduct')

    def __repr__(self):
        return f'{self.submenu} {self.product_name}'

class CartProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart = db.relationship('Cart', secondary=cart_products, backref=db.backref('cart_products', lazy='dynamic'))
    product = db.Column(db.Integer(), db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer(), default=1)
    product_price = db.Column(db.Integer(), default=0)
    final_price = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return f'{self.product}'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Integer(), db.ForeignKey('customer.id'))
    cart = db.Column(db.Integer(), db.ForeignKey('cart.id'))
    number = db.Column(db.Integer(), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    delivery = db.Column(db.String(50))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)



