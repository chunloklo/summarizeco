from flask import Flask
from flask import request
from flask import render_template
from summary import Summary
from crawler import jobSearch
from buzzWords import BuzzWords
from update import newsSearch

app = Flask(__name__)
app.config["SECRET_KEY"]

@app.route('/')
def textform(name = None):
    return render_template("hello2.html", name = name)

@app.route('/', methods=['POST'])
def testform_post():
    text = request.form['text']
    major = request.form['major']
    jobType = request.form['jobType']
    s=Summary()
    processed_text = s.getSummary(text)

    bW=BuzzWords()
    b = bW.findBuzzWords(text, 1)
    processed_buzz = b[0]+", "+b[1]+", "+b[2]

    news = newsSearch(text)

    jobList = jobSearch(major, text, jobType)
    return render_template("result.html", company = text,
        summary = processed_text, buzzWords = processed_buzz,
            jobList = jobList, news = news)

if __name__ == '__main__':
    app.run()