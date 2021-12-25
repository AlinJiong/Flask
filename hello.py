from flask import Flask, redirect, url_for, request, render_template

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


# URL, 反向路由url_for, func
app.add_url_rule('/hello', 'hello_world', hello_world)

if __name__ == '__main__':
    app.run(debug=True)
