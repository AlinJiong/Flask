from flask import Flask, render_template, request, flash
from forms import LoginForm

app = Flask(__name__)
app.secret_key = "aaasdsdadfda"


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.data)
            return render_template('contact.html', form=form)
        else:
            return 'success'
    else:
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)