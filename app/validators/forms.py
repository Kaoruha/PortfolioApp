from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, length, Regexp
from wtforms import ValidationError
from app.models.user import User

from app.validators.base import BaseForm
from wtforms import Form


class ClientForm(BaseForm):
    account = StringField(validators=[
        DataRequired(message='不允许为空'),
        length(min=4, max=32)
    ])
    password = StringField()


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])


class UserFilterForm(BaseForm):
    start_row = IntegerField()
    count = IntegerField()
    account_filter = StringField()
    sort_by = StringField()
    descending = BooleanField()
