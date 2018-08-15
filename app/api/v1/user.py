from flask import Blueprint, jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # 验证token是否合法， 是否过期
    user = User.query.filter_by(id=uid).first_or_404()
    # r = {
    #     'nickname':user.nickname,
    #     'email':user.email,
    # }
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    # 普通用户查询用户接口
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
def super_delete_user():
    pass


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 获取验证通过后，存放在g变量中的uid
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['PUT'])
def update_user():
    return 'hello world'\

