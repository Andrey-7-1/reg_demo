import json

from flask import Flask, request, render_template, redirect, abort, url_for, send_from_directory

from forms.user import RegisterForm
from save_utils import save_to_csv, update_orgs, update_division_type_name

from flaskwebgui import FlaskUI

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app_ui = FlaskUI(app, width=500, height=500)  # Ui For the app


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    data = json.load(open('data/user_reg_options.json'))
    form = RegisterForm()

    # Form submitted
    if form.validate_on_submit() or request.method == 'POST':
        try:
            full_pos = (form.position_type.data + ' ' +
                     data['6']['result'][data['6']['normal'].index(form.division_type.data)] + ' ' +
                     form.division_type_name.data).strip()
        except ValueError:
            full_pos = (form.position_type.data + ' ' +
                        form.division_type.data + ' ' +
                        form.division_type_name.data).strip()

        user = (form.org_name_full.data,
                form.org_name_short.data,
                form.division_name.data,
                form.position_level.data,
                form.position_type.data,
                form.division_type.data,
                form.division_type_name.data,
                full_pos,
                form.surname.data,
                form.name.data,
                form.patronymic.data,
                form.phone.data,
                form.email.data,
                form.reg_day_num.data, form.reg_month_num.data, form.reg_year_num.data,
                form.reg_hour_num.data, form.reg_minute_num.data,
                form.account_id.data)

        save_to_csv('data/users.csv', user)
        update_orgs('data/user_reg_options.json', form.org_name_full.data, form.org_name_short.data)
        update_division_type_name('data/user_reg_options.json', form.division_type_name.data)
        return redirect(url_for('success'))

    # Note: Wrong keys might be used!!!

    dn_options_type = data['11']
    dn_options = {"Аппарат_управления": data['7']['normal'],
                  "Структурное_подразделение": data['8']['normal'],
                  "Филиал": data['9']['normal']}
    pt_options = data['2'] + data['3'] + data['4']  # Maybe make only valid options show up?
    pt_level_ref = {"specialist": data['2'], "supervisor": data['3'] + data['4']}
    dt_options = data['6']

    return render_template('register.html', form=form,
                           dn_options_type=dn_options_type,
                           dn_options=dn_options,
                           pt_options=pt_options,
                           pt_level_ref=pt_level_ref,
                           dt_options=dt_options)


@app.route('/data', methods=['GET', 'POST'])
def data():
    # Check if request is authorised
    if request.method == 'POST':
        if request.form['code'] != '12345':
            abort(403)
        else:
            return send_from_directory('data', 'users.csv')
    return render_template('auth.html')


@app.route('/success')
def success():
    return redirect(url_for('index'))


if __name__ == '__main__':
    debug = 0
    if debug:
        app.run()
    else:
        app_ui.run()
