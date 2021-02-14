from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, SelectField, TextAreaField, FormField, FieldList
from wtforms.validators import Email, DataRequired, Length, EqualTo, required
from wtforms.fields.html5 import TelField, EmailField

from wtforms.widgets import CheckboxInput



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email('Некорректный email')])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=5, max=100,
                                                                          message='Пароль должен быть от 5 до 100 символов')])
    remember = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired(), Length(max=100, message='Имя не должно превышать 100 символов')])
    email = StringField('Email', validators=[Email('Некорректный email')])
    password1 = PasswordField('Пароль', validators=[DataRequired(), Length(min=5, max=100,
                                                                           message='Пароль должен быть от 5 до 100 символов')])
    password2 = PasswordField('Повторите пароль',
                              validators=[DataRequired(),
                                          Length(min=5, max=100, message='Пароль должен быть от 5 до 100 символов'),
                                          EqualTo('password1', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')




class OrderForm(FlaskForm):
    CHOICE = [('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')]

    first_name = StringField('Имя', validators=[DataRequired(), Length(max=100,
                                                                   message='Максимальная длинна имени 100 символов')])
    last_name = StringField('Фамилия', validators=[DataRequired(), Length(max=100,
                                                                  message='Максимальная длинна фамилии 100 символов')])
    email = EmailField('Email', validators=[Email('Некорректный email')])
    phone = TelField('Телефон', validators=[DataRequired(), Length(max=12,
                                                                   message='Максимальная длина номера телефона 12 символов')])
    delivery = SelectField('Доставка', choices=CHOICE)
    address = TextAreaField('Адрес доставки')
    submit = SubmitField('Подтвердить заказ')


class SortForm(FlaskForm):
    SORT = [('id', 'умолчанию'), ('price', 'возрастанию цены'), ('-price', 'убыванию цены')]

    sort = SelectField('Сортировать по:', choices=SORT)
    min_price = StringField('Цена от')
    max_price = StringField('Цена до')
    exist = BooleanField('В наличие')
    submit = SubmitField('Применить')








