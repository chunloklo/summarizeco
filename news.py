import json
from eventregistry import *
from datetime import timedelta, date
import sys

def retrieveNews():
    companyName = ''
    for index in range(1,len(sys.argv)-1):
        companyName += sys.argv[index] + " "
    companyName += sys.argv[len(sys.argv)-1]
    print companyName
    
    er = EventRegistry()
    q = QueryArticles(keywords="company", lang="eng")
    #set the date limit of interest
    #q.setDateLimit((date.today() + timedelta(days=-2)),date.today())
    q.addConcept(er.getConceptUri(companyName))

    q.addRequestedResult(RequestArticlesInfo(page = 1, count = 40,
        returnInfo = ReturnInfo(articleInfo = ArticleInfoFlags(title=True,
            basicInfo=True))))
    #print json.dumps(er.execQuery(q), sort_keys=True,
    #                 indent=4, separators=(',', ': '))
    e = er.execQuery(q)
    j = json.loads(json.dumps(e))
    total = 0;
    
    
    articleSet = set();
    while(len(articleSet) < 5):
        if companyName.lower() in j['articles']['results'][total]['title'].lower():
            articleSet.add(j['articles']['results'][total]['title']+'^'+j['articles']['results'][total]['url']+'^'+j['articles']['results'][total]['date']+'\n')
            #print j['articles']['results'][total]['title'],j['articles']['results'][total]['url'],j['articles']['results'][total]['date']
        total+=1
        if total == 39:
            break;     
    with open("articles.txt", "w") as text_file:
        text_file.write("".join(str(e) for e in articleSet))

retrieveNews()