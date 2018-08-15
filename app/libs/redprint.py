

class Redprint:

    def __init__(self,name):
        self.name = name
        self.mound = []


    def route(self, rule, **options):
        """实现红图的路由注册装饰器"""
        def decorator(f):
            # endpoint = options.pop("endpoint", f.__name__)
            # self.add_url_rule(rule, endpoint, f, **options)
            self.mound.append((f,rule,options))
            return f

        return decorator


    def register(self, bp, url_prefix=None):
        '''蓝图的注册'''
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f,rule,options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
