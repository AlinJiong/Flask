from flask import Flask, redirect, url_for

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


# URL, 反向路由url_for, func
app.add_url_rule('/hello', 'hello_world', hello_world)

if __name__ == '__main__':
    app.run(debug=True)