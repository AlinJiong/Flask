from flask import Flask, redirect, url_for, request, render_template
from flask.helpers import make_response

app = Flask(__name__)


# 127.0.0.1:5000/
@app.route('/')
def hello():
    return 'Hello world'


# 127.0.0.1:5000/hello
def hello_world():
    return 'hello world'


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/index')
def index():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {'name': 'xiaoming', 'age': 18}
    # return render_template('index.html',
    #                        my_str=my_str,
    #                        my_int=my_int,
    #                        my_array=my_array,
    #                        my_dict=my_dict)

    #拆包传入数据
    return render_template('index.html', **locals())


@app.route('/test_static')
def test_static():
    return render_template('test_staic.html')


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", **locals())


# cookie 操作
@app.route('/set_cookies')
def set_cookie():
    resp = make_response('success')  #设置响应体
    resp.set_cookie('alin', 'alin', max_age=3600)
    return resp


@app.route('/get_cookies')
def get_cookie():
    cookie_1 = request.cookies.get('alin')
    return cookie_1


@app.route('/del_cookies')
def del_cookie():
    resp = make_response('del cookies')
    resp.delete_cookie('alin')
    return resp


# URL, 反向路由url_for, func
app.add_url_rule('/hello', 'hello_world', hello_world)

if __name__ == '__main__':
    app.run(debug=True)
