from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def textform(name = None):
    return render_template("hello.html", name = name)

@app.route('/', methods=['POST'])
def testform_post():
    print("working...")
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == '__main__':
    app.run()