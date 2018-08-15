from werkzeug.exceptions import HTTPException
from flask_cors import CORS

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError



app = create_app()
CORS(app)
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        raise e
        code = e.code
        msg = e.description
        error_code = 1007

        return APIException(msg,code,error_code)
    else:
        # LOG日志记录
        # if not app.config['DEBUG']:
        #     return ServerError()
        # else:
        print('\033[31m '+str(e)+' \033[0m')
        raise e





if __name__ == '__main__':
    app.run('0.0.0.0',debug=app.config['DEBUG'],port=3001)