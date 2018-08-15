from app.app import Flask


def register_blueprints(app):
    """2.在app中注册蓝图"""
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/v1')


def register_plugins(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    pass


def create_app():
    """1.初始化flask app核心对象"""
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugins(app)

    return app
