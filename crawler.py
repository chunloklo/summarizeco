import urllib.request
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

def indeedSearch(keyword = "", company = "", jobType = ""):
    url = "http://api.indeed.com/ads/apisearch?" + \
    "publisher=7279967959911398" + \
    "&format=json&q={0}%20company:{1}".format(keyword, company) + \
    "&st=employer&jt={0}".format(jobType) + \
    "&sort=&start=&limit=100&fromage=all&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2"
    response = urllib.request.urlopen(url)
    json_data = json.loads(response.read().decode("utf-8"))
    jobList = []
    for jobs in json_data["results"]:
        if jobs["jobtitle"] not in jobList:
            jobList.append(jobs["jobtitle"])
    return jobList

def jobSearch(keyword = "", company = "", jobType = ""):
    company = "+".join(company.split())
    print(company)
    jobList = indeedSearch(keyword, company, jobType)
    jobList1 = indeedSearch("", company, jobType)
    for job in jobList1:
        if job not in jobList:
            jobList.append(job)
    jobList = jobList[:6]
    return jobList


# keyword = ""
# company = "dfsfsdf"
# jobType = ""
# #internship, full time, part time
# jobList = jobSearch(keyword, company, jobType)
# for job in jobList:
#     print(job)