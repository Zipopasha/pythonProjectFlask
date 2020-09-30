from core import app

from flask import render_template, redirect
from core import db
# from model import Unit

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

@app.route('/startpage')
def startpage():
    return 'STARTPAGE'


class UnitForm(FlaskForm):
    name = StringField('Name here', validators=[DataRequired()])
    health = IntegerField('Health here', validators=[DataRequired()])
    submit = SubmitField('--> Add Unit Herte <--')


@app.route('/startpage', methods=['GET', 'POST'])
def startpage():
    # res = dir(request)
    form = UnitForm()

    if form.validate_on_submit():
        print(form.name, form.health)

        db.session.add(Unit(name=form.name.data, health=form.health.data))
        db.session.commit()
        return redirect('/unitall')
    return render_template('startpage.html', form=form)


@app.route('/unitall')
def unitall():

    units = Unit.query.all()
    data = dict(enumerate(units))

    return str(data)
