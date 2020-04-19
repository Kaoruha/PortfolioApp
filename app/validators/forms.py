from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Regexp
from wtforms import ValidationError
from app.models.user import User

from app.validators.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(validators=[
        DataRequired(message='不允许为空'),
        length(min=5, max=32)
    ])
    secret = StringField()



class TokenForm(BaseForm):
    token = StringField(validators=[DataRequired()])
