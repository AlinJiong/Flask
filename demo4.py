from flask_mail import FlaskMailUnicodeDecodeError, Mail, Message
from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'from@qq.com'
app.config['MAIL_PASSWORD'] = '**************'

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('hello',
                  sender='from@qq.com',
                  recipients=['to@qq.com'])
    msg.body = "send by flask"
    mail.send(msg)
    return "send success"


if __name__ == '__main__':
    app.run(debug=True)