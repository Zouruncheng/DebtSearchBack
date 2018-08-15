
from app import create_app
from app.models.base import db
from app.models.user import User


# 生成管理员
# app = create_app()
# with app.app_context():
#     with db.auto_commit():
#         # 创建一个超级管理员
#         user = User()
#         user.nickname = 'Super'
#         user.password = '123456'
#         user.email = '999@qq.com'
#         user.auth = 2
#         db.session.add(user)



# class QiYue1():
#     name = 'qiyue'
#     age = 18
#
#     def __init__(self):
#         self.gender = 'male'
#
#
#     def keys(self):
#         return ('name',)
#
#
#     def __getitem__(self, item):
#         return getattr(self,item)


# o = QiYue1()
# print(dict(o))

def sor():
    li=[{1:"b"},{3:"c"},{2:"a"}]
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            v1= [li[j][key] for key in li[j].keys()][0]
            v2= [li[j+1][key] for key in li[j+1].keys()][0]
            print(v1,v2)
            if ord(v1) > ord(v2):
                li[j],li[j+1] = li[j+1],li[j]
    return li




def sor2():
    li=[{1:"b"},{3:"c"},{2:"a"}]
    li.sort(index=[list(li[i].values())[0] for i in range(len(li))])
    return li



if __name__ == '__main__':
    print(sor2())