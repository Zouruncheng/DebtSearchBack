from app.libs.redprint import Redprint
from app.validators.forms import ClientForm,UserEmailForm
from app.libs.enums import ClientTypeEnum
from flask import request
from werkzeug.exceptions import HTTPException
from app.libs.error_code import ClientTypeError, Success

from app.models.user import User

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 表单和json区别
    # request.json接收到json数据
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        ClientTypeEnum.USER_MINA:__register_user_by_mina,

    }
    # 从枚举中直接调用注册函数
    promise[form.sign_type.data]()


    return Success()


def __register_user_by_email():
    # email注册
    form = UserEmailForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:__register_user_by_email,
        ClientTypeEnum.USER_MINA:__register_user_by_mina,
    }
    # 注册
    print(form.nickname, form.account, form.secret)
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)



def __register_user_by_mina(form):
    # 小程序注册


    pass