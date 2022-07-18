from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired
from datetime import datetime


# TODO: Add datalists!

class RegisterForm(FlaskForm):
    placeholder_common = "Начните вводить название или выберите из перечня"

    # Company details
    org_name_full = StringField('Название организации (полное)', validators=[DataRequired()],
                                render_kw={'placeholder': 'Введите название'})
    org_name_short = StringField('Название организации (краткое)', validators=[DataRequired()],
                                 render_kw={'placeholder': 'Введите название'})
    division_name = StringField('Укажите ваше подразделения', validators=[DataRequired()], render_kw={'placeholder': "Заполните поле вверху"})

    # Employment details
    position_level = SelectField('Ваш должностной уровень', validators=[DataRequired()],
                                 choices=['Руководитель', 'Специалист'])
    position_type = StringField('Укажите тип должности', validators=[DataRequired()],
                                render_kw={'placeholder': placeholder_common})
    division_type = StringField('Укажите к какому типу подразделения относится ваша должность',
                                validators=[DataRequired()], render_kw={'placeholder': placeholder_common})
    division_type_name = StringField('Введите наименование указанного выше подразделения', validators=[DataRequired()],
                                     render_kw={'placeholder': 'Введите название'})
    # Position is auto generated based on the above

    # ФИО
    surname = StringField('Фамилия', validators=[DataRequired()], render_kw={'placeholder': 'Введите вашу фамилию'})
    name = StringField('Имя', validators=[DataRequired()], render_kw={'placeholder': 'Введите ваше имя'})
    patronymic = StringField('Отчество', validators=[DataRequired()], render_kw={'placeholder': 'Введите ваше отчество'})

    # Contact info
    phone = StringField('Рабочий телефон', validators=[DataRequired()], render_kw={'placeholder': '+7 (000) 000-00-00'})
    email = EmailField('E-mail (рабочий)', validators=[DataRequired()], render_kw={'placeholder': 'Введите ваш email'})

    # System info
    # Not using a unix timestamp due to data being exported to csv&Excel, not an SQL database
    reg_day_num = IntegerField(default=datetime.now().day)
    reg_month_num = IntegerField(default=datetime.now().month)
    reg_year_num = IntegerField(default=datetime.now().year)
    reg_hour_num = IntegerField(default=datetime.now().hour)
    reg_minute_num = IntegerField(default=datetime.now().minute)
    account_id = StringField(default='CODE1')  # This would be a unique ID in production

    submit = SubmitField('Зарегистрироваться')