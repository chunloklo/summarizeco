import subprocess
import csv

def callNews(companyName):
    s = 'py -2 news.py ' + companyName;
    subprocess.call(s, shell=True)

def parseArticles():
    d = {}
    d['Title'] = []
    d['URL'] = []
    d['Date'] = []
    dictReader = csv.DictReader(open('articles.txt', 'r'), fieldnames = ['Title', 'URL',
        'Date'], delimiter = '^')
    for row in dictReader:
        for key in row:
            d[key].append(row[key])
    return d