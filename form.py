from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm, CSRFProtect


class Form(FlaskForm):
    name = StringField(validators=[DataRequired()])
    coffee_price = StringField(validators=[DataRequired()], default='£')
    map_url = StringField(validators=[DataRequired()])
    img_url = StringField(validators=[DataRequired()])
    seats = StringField(validators=[DataRequired()])
    location = StringField(validators=[DataRequired()])

    has_wifi = BooleanField()
    has_socket = BooleanField()
    has_toilet = BooleanField()
    can_take_calls = BooleanField()
    submit = SubmitField()


class DeleteCafe(FlaskForm):
    Cafe_id = IntegerField(validators=[DataRequired()])
    api_key = StringField(validators=[DataRequired()])
    submit = SubmitField()