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
    num_of_links = None
    broken_links = []
    count = None
    not_found_count = None

    if request.method == 'GET':
        return render_template("index.html", form=form)
    if form.validate_on_submit:
        link = form.url.data
        url = HandleRequest()
        url.default_form_url = form.url.data
        expected_url = url.check_url(url.default_form_url)
        url.process_url(expected_url)
        
        # Getting Values From the Parent Class
        title_tag = url.title_tag
        num_of_links = url.num_of_links_found
        broken_links = url.broken_links
        count = url.count
        not_found_count = url.not_found_count

        num = 0

        return render_template("index.html", link=link, title_tag=title_tag, num_of_links=num_of_links, broken_links=broken_links, count=count, not_found_count=not_found_count, num=num, form=form)


if __name__ == "__main__":
    app.run(debug=False)