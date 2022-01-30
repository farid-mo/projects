from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)

@app.route("/contact_process", methods=['POST', 'GET'])
def submit_form():
    return 'form submitted hooray!'