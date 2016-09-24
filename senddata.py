from flask import Flask
from flask import request
from flask import render_template
from summary import Summary
from crawler import jobSearch
from buzzWords import BuzzWords

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

    bW=BuzzWords()
    b = bW.findBuzzWords(text, 1)
    processed_buzz = ""
    if len(b) >= 3:
        processed_buzz = b[0]+", "+b[1]+", "+b[2]
    elif len(b) ==2:
        processed_buzz = b[0]+", "+b[1]
    elif len(b) == 1:
        processed_buzz = b[0]


    jobList = jobSearch(major, "text", "")
    return render_template("result.html", company = text,
        summary = processed_text, buzzWords = processed_buzz, jobList= jobList)

if __name__ == '__main__':
    app.run()