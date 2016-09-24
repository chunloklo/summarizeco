import subprocess

def callNews(companyName):
    s = 'py -2 news.py ' + companyName;
    subprocess.call(s, shell=True)