from flask import Flask
from flask import request
from flask import render_template
from summary import Summary
from crawler import jobSearch
from buzzWords import BuzzWords
from update import newsSearch

app = Flask(__name__)

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
    processed_buzz=""
    if(len(b)>=3):
        processed_buzz = b[0]+", "+b[1]+", "+b[2]
    elif(len(b)==2):
        processed_buzz = b[0]+", "+b[1]
    elif(len(b)==1):
        processed_buzz = b[0]

    news = newsSearch(text)

    jobList = jobSearch(major, text, jobType)
    return render_template("result.html", company = text,
        summary = processed_text, buzzWords = processed_buzz,
            jobList = jobList, news = news)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run()