# 封装路由
import base64
import os
import time

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('settings.py')
CORS(app, resources=r'/*')

# 记录商品存储的数据库
db = SQLAlchemy(app)


# 数据库查找到的数据解析
def data_conversion(data):
    data_list = []
    if not data:
        return '无数据'
    for i in data:
        # 对图片的地址进行处理
        # print(i.img.split('/', 7)[-1])
        i.img = i.img.split('/', 8)[-1]
        print(i.img)
        data_dict = {'Id': i.Id, 'price': i.price, 'value': i.value, 'img': i.img, 'title': i.title}
        data_list.append(data_dict)
    return jsonify(data_list)


class shopping(db.Model):
    __tablename__ = 'shopping'
    Id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True, index=True)  # id自增长
    price = db.Column(db.Float, nullable=False, default=0)
    value = db.Column(db.Integer, nullable=False, default=0)
    img = db.Column(db.String(100), nullable=False, default='')
    title = db.Column(db.String(100), nullable=False, default='')
    db.create_all()


# 添加/存储
@app.route('/add', methods=['POST'])
def add():
    # 获取前端发送的数据
    if request.method == 'POST':
        # 对发送的图片数据进行处理
        data = request.get_json()
        img_url_data = data['img'].split(',')[1]
        image_data = base64.b64decode(img_url_data)
        filename = '/Users/yujunxiong/Desktop/Vueproject/backstage/src/assets/image/' + str(int(time.time())) + '.jpeg'
        with open(filename, 'wb') as f:
            f.write(image_data)
        h = shopping(price=float(data['price']), value=int(data['value']), img=filename, title=data['title'])
        db.session.add(h)
        db.session.commit()
        print(data['title'])
    return "添加失败"


# 根据主键删除数据库中的数据
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        data = request.get_json()
        img_file = shopping.query.filter_by(Id=data['id']).all()[0].img
        shopping.query.filter_by(Id=data['id']).delete()
        db.session.commit()
        db.session.close()
        os.remove(img_file)
        return '成功'
    return '删除'


# 搜索
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        data = request.get_json()
        query_content = '%' + data['value'] + '%'
        result = shopping.query.filter(shopping.title.like(query_content)).all()
        data_list = []
        if not data:
            return '无数据'
        for i in result:
            # 对图片的地址进行处理
            # print(i.img.split('/', 7)[-1])
            i.img = i.img.split('/', 8)[-1]
            print(i.img)
            data_dict = {'Id': i.Id, 'price': i.price, 'value': i.value, 'img': i.img, 'title': i.title}
            data_list.append(data_dict)
        return jsonify(data_list)
    return "请求成功"


# 更改数据,1.获取前端传来的id，返回查询到id对应的值
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        front_data = request.get_json()
        if "img" in front_data:  # 此情况为img图片信息做了更新
            if front_data["img"] != '':
                print(front_data)
                img_url_data = front_data['img'].split(',')[1]
                image_data = base64.b64decode(img_url_data)
                filename = '/Users/yujunxiong/Desktop/Vueproject/backstage/src/assets/image/' + str(
                    int(time.time())) + '.jpeg'
                with open(filename, 'wb') as f:
                    f.write(image_data)
                imgUrl = shopping.query.filter_by(Id=front_data['id']).first().img
                shopping.query.filter_by(Id=front_data['id']).update(
                    {'price': front_data['price'], 'value': front_data['value'], 'img': filename,
                     'title': front_data['title']})
                db.session.commit()
                db.session.close()
                os.remove(imgUrl)
                return '修改成功'
            else:  # 此情况为img图片没做更新
                shopping.query.filter_by(Id=front_data['id']).update(
                    {'price': front_data['price'], 'value': front_data['value'],
                     'title': front_data['title']})
                db.session.commit()
                db.session.close()
                return '没有跟新图片数据'
        else:
            # 查询出来的数据
            data = shopping.query.filter_by(Id=front_data['id']).first()
            data.img = data.img.split('/', 8)[-1]
            result = {'Id': data.Id, 'price': data.price, 'value': data.value, 'img': data.img, 'title': data.title}
            return jsonify(result)


# 数据排序
@app.route('/sort', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        data = request.get_json()
        # 按照价格进行排序
        if data['mode'] == 'price':
            results = shopping.query.order_by(shopping.price.desc()).all()
            return data_conversion(results)
        # 按照默认的排序方式
        if data['mode'] == 'default':
            data = shopping.query.all()
            return data_conversion(data)
        if data['mode'] == 'number':
            results = shopping.query.order_by(shopping.value.desc()).all()
            return data_conversion(results)
        if data['mode'] == '':
            return '无'


# 展示数据
@app.route('/getdata', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        data_list = []
        data = shopping.query.all()
        if not data:
            return '无数据'
        for i in data:
            # 对图片的地址进行处理
            # print(i.img.split('/', 7)[-1])
            i.img = i.img.split('/', 8)[-1]
            print(i.img)
            data_dict = {'Id': i.Id, 'price': i.price, 'value': i.value, 'img': i.img, 'title': i.title}
            data_list.append(data_dict)

        return jsonify(data_list)
    else:
        return '请求失败'


if __name__ == '__main__':
    # 创建数据库
    db.create_all()
    app.run()
