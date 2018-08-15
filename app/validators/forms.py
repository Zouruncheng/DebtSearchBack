from flask import request
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired,Length,Email,Regexp
from wtforms import ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    """验证Client参数"""
    account = StringField(validators=([DataRequired(message='账户不能为空'),Length(min=5,max=32)]))
    secret = StringField()

    # 登录类型
    sign_type = IntegerField(validators=[DataRequired()])


    def validate_sign_type(self,value):
        # 验证登录类型
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.sign_type.data = client




class UserEmailForm(ClientForm):
    '''EMAIL用户注册'''
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       Length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class BookSearchForm(Form):

    q = StringField(validators=[DataRequired()])


















