class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123@localhost:5433/flask_db'

    SECRET_KEY = 'd#4bg=2ov3)j5o=*i&%jl=@$(&sf$0s!g%cnj!gybg6(*dt%ed'
    SECURITY_PASSWORD_SALT = 'SALT'
    SECURITY_PASSWORD_HASH = 'bcrypt'

    PRODUCTS_PER_PAGE = 2
