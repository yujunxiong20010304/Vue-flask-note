# flask文件配置
User = 'yujunxiong'
Password = 'yjx20010304'
Database = 'shoppingCartBackground'
Port = 3306
Ip = '47.109.23.208'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(User, Password, Ip, Port, Database)
SQLALCHEMY_TRACK_MODIFICATIONS = False
ENV = 'development'
DEBUG = True

