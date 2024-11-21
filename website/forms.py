from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class Contact_Me(FlaskForm):
    name = StringField('Your Name*', validators=[DataRequired()])
    email = EmailField('Your Email*', validators=[DataRequired(), Email()])
    textarea = TextAreaField('Your Message', validators=[DataRequired()])
    submitbtn = SubmitField('Send Message')
    test = StringField('1 + 5', validators=[DataRequired()])