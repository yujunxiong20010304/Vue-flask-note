# 封装数据库的操作
from flasks import shopping


class operationDatabase(object):
    def __init__(self):
        self.db = shopping()

    # 存储
    def add(self):
        us1 = shopping(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)


    # 删除
    def delete(self):
        pass

    # 更新
    def update(self):
        pass

    # 搜索
    def search(self):
        pass

    # 排序
    def sort(self):
        pass
