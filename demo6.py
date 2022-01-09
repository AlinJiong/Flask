from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'test'
PASSWORD = 'mysql824.'

DA_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE)

# 指定使用的数据库
app.config['SQLALCHEMY_DATABASE_URI'] = DA_URI
# 跟踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建一个SQLAlchemy对象,需要放在config后面
db = SQLAlchemy(app)


@app.route('/')
def test():
    engine = db.get_engine()

    with engine.connect() as conn:
        result = conn.execute('select 1')
        print(result.fetchone())
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)