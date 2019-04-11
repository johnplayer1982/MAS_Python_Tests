from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/')
def my_form():
    return render_template('link-checker.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

def hello():
    return 'Hello, World!'
