from flask import Flask, render_template, url_for, flash
from flask_wtf import FlaskForm
import requests, urllib.request
from views.forms import UrlForm


app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/', methods=['GET','POST'])
def index():
    form = UrlForm()
    if form.validate_on_submit:
        # form_url = form.url.data
        pass
        # response = urllib.request.urlopen(form_url)
        # print(response)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)