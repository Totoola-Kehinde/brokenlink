from flask import Flask, render_template, url_for, flash
from flask_wtf import FlaskForm
from views.forms import UrlForm
from controllers.handlerequest import HandleRequest


app = Flask(__name__)
app.secret_key = 'mysecretkey'

handler = HandleRequest()


@app.route('/', methods=['GET','POST'])
def index():
    form = UrlForm()
    if form.validate_on_submit:
        handler.check_url(form.url.data)
        handler.process_url(form.url.data)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)