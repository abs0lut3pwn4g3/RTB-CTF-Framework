from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class UserHashForm(FlaskForm):
    userHash = StringField('User hash',
                           validators=[
                               DataRequired(),
                               Length(min=32, max=32)
                           ]
                           )
    submit = SubmitField('Submit')


class RootHashForm(FlaskForm):
    rootHash = StringField('Root hash',
                           validators=[
                               DataRequired(),
                               Length(min=32, max=32)
                           ]
                           )
    submit = SubmitField('Submit')
