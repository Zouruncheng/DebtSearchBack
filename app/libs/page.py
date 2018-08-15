class PageInfo():
    """
    :param current_page: 当前页码
    :param all_count: 数据库总行数
    :param per_page: 每页显示行数
    :param base_url: 基本路径
    :param show_page: 每页显示页码数
    """
    def __init__(self,current_page, all_count, per_page=10,):
        # 防止页面的非法输入
        try:
            self.current_page = int(current_page)
        except Exception as e:
            # 非法输入时跳到首页
            self.current_page = 1
        self.per_page= per_page
        a, b = divmod(all_count, per_page)
        if b:
            a = a+1
        self.all_pager = a # 数据总共有多少页

    def start(self):
        return (self.current_page - 1) * self.per_page

    def end(self):
        return self.current_page * self.per_page
