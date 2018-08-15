# 用户权限配置文件
class Scope:
    ''''''
    allow_api = []
    allow_module = []
    forbidden = []
    def __add__(self,other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self
    # 运算符重载支持对象相加


class AdminScope(Scope):
    '''管理员视图函数权限'''
    allow_api = ['v1.user+super_get_user','v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    '''普通用户视图函数权限'''
    forbidden = ['v1.user+super_get_user','v1.user+super_delete_user']
    # allow_api = ['v1.user+get_user','v1.user+delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    '''判断是否在权限列表'''
    # 让endpoint支持所在module
    # endpoint = v1.red_name+view_func
    gl = globals()
    scope = gl.get(scope)()
    module_name = endpoint.split('+')[0]
    if endpoint in scope.forbiden:
        return False
    if endpoint in scope.allow_api:
        return True
    if module_name in scope.allow_module:
        return True
    else:
        return False