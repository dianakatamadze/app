from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField,IntegerField
from  wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя Фамилия', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Контактная почта', validators=[DataRequired()])
    telephone = IntegerField('Телефон',validators=[DataRequired()])
    adress = StringField('Адрес доставки', validators=[DataRequired()])
    bank = IntegerField('Номер банковской карты для оплаты',validators=[DataRequired()])
    remember_me = BooleanField('Запомнить данные')
    submit = SubmitField('Оформить покупку')
    