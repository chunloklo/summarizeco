from flask import Flask
from flask import request
from flask import render_template
from summary import Summary

app = Flask(__name__)

@app.route('/')
def textform(name = None):
    return render_template("hello.html", name = name)

@app.route('/', methods=['POST'])
def testform_post():
    print("working...")
    text = request.form['text']
    s=Summary()
    processed_text = s.getSummary(text)
    return processed_text

if __name__ == '__main__':
    app.run()