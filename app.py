from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security

from config import Config
from flask import render_template


app = Flask(__name__)
app.config.from_object(Config)



db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand) #- создаём команду "db" в консоли

login_manager = LoginManager(app)
login_manager.login_message = 'Авторизуйтесь для доступа к закрытым страницам'
login_manager.login_view = 'login' # эта функция делает так, что если неавторизованный пользователь поподает на страницу,
#которая закрыта для него, то вместо ошибки, его перенаправляют на страницу авторизации



""" Admin """

from models import *

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(MainMenu, db.session))
admin.add_view(ModelView(Submenu, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Cart, db.session))
admin.add_view(ModelView(Customer, db.session))
admin.add_view(ModelView(CartProduct, db.session))
admin.add_view(ModelView(Order, db.session))

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)


""" Blueprint """

from menu.menu import menu
from cart.cart import cart
app.register_blueprint(menu, url_prefix='/catalog')
app.register_blueprint(cart, url_prefix='/cart')


"""Ошибки"""

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500