from flask import Blueprint

from app.api.v1 import book,user,client,token,gift,debt



def create_blueprint_v1():
    """注册v1蓝图"""
    bp_v1 = Blueprint('v1', __name__)
    # 注册红图api到蓝图
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    gift.api.register(bp_v1)
    debt.api.register(bp_v1)
    return bp_v1
