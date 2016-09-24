from flask import Flask
from flask import request
from flask import render_template
from summary import Summary
from crawler import jobSearch

app = Flask(__name__)

@app.route('/')
def textform(name = None):
    return render_template("hello2.html", name = name)

@app.route('/', methods=['POST'])
def testform_post():
    text = request.form['text']
    major = request.form['major']
    s=Summary()
    processed_text = s.getSummary(text)
    jobList = jobSearch(major, "text", "")
    return render_template("result.html", company = text, summary = processed_text)

if __name__ == '__main__':
    app.run()