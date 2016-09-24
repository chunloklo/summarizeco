import urllib.request
from urllib.request import urlopen
import feedparser

def indeedSearch(company = ""):
    url = "http://news.google.com/news?q={0}".format(company) + \
        "&output=rss"
    response = feedparser.parse(url)
    responses = []
    if(response['entries'].length >= 1):
        responses.append(response['entries'][0]['title'])
    if(response['entries'].length >= 2):
        responses.append(response['entries'][1]['title'])
    if(response['entries'].length >= 3):
        responses.append(response['entries'][2]['title'])
    return responses
# def jobSearch(keyword = "", company = "", jobType = ""):
#     jobList = indeedSearch(keyword, company, jobType)
#     jobList1 = indeedSearch("", company, jobType)
#     for job in jobList1:
#         if job not in jobList:
#             jobList.append(job)
#     return jobList

# print(indeedSearch("ionic+security"))