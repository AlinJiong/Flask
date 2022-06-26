import os
import uuid
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'


@app.route('/upload', methods=['GET', "POST"])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    else:
        f = request.files['file']
        print(request.files)
        filename = uuid.uuid4().hex + '.' + f.filename.split('.')[-1]
        print(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))

        return '文件上传成功！'


if __name__ == '__main__':
    app.run(debug=True)
