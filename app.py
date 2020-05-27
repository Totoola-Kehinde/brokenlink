from flask import Flask, render_template, url_for, flash, request
from flask_wtf import FlaskForm
from views.forms import UrlForm
from controllers.handlerequest import HandleRequest


app = Flask(__name__)
app.secret_key = 'mysecretkey'

handler = HandleRequest()


@app.route('/', methods=['GET','POST'])
def index():
    form = UrlForm()

    # View Objects
    title_tag = None
    if request.method == 'GET':
        return render_template("index.html", form=form)
    if form.validate_on_submit:
        url = HandleRequest()
        url.default_form_url = form.url.data
        expected_url = url.check_url(url.default_form_url)
        url.process_url(expected_url)
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)