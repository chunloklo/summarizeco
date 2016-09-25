import re
import wikipedia
class BuzzWords:
    def correctName(self,name):
        results = wikipedia.search(name,7)
        for result in results:
            try:
                for category in wikipedia.WikipediaPage(result).categories:
                    category=category.lower()
                    if "software" in category or "comput" in category or "internet" in category or "invest"in category:
                        return result
            except:
                print("Error")
        if(len(results)>=1):
            return result[0]
        return ""
    def getBuzzWords(self):
        buzzWords={}
        with open("buzzWords.txt") as f:
            bw = f.readlines()
        bwn=[]
        for b in bw:
            b=b.strip()
            bwn.append(b)
        for item in bwn:
            buzzWords[item]=0
        return buzzWords
    def getContents(self,name):
        try:
            content = wikipedia.page(name).content
            return content
        except wikipedia.exceptions.DisambiguationError as ex:
            content = wikipedia.page(ex.args[1][0]).content
            return content


    def findBuzzWords(self,name,k):
        name=self.correctName(name)
        if(name==""):
            print("no cs company found for query")
        contents = self.getContents(name)

        buzzWords=self.getBuzzWords()

        regex = re.compile('[^a-zA-Z]')

        approvedBuzzWords=[]

        content=contents.split()
        for i in range(0,len(content)-1):
            s = regex.sub('', content[i])+" "+regex.sub('', content[i+1])
            s1= regex.sub('', content[i])
            s=s.lower()
            s1=s1.lower()
            if s in buzzWords.keys():
                buzzWords[s]=buzzWords[s]+1
            if s1 in buzzWords.keys():
                buzzWords[s1]=buzzWords[s1]+1
        for key in buzzWords.keys():
            if buzzWords[key]>k:
                approvedBuzzWords.append([key,buzzWords[key]])

        approvedBuzzWords=sorted(approvedBuzzWords,key=lambda x: x[1])
        approvedBuzzWords.reverse()

        finalArray=[]
        for a in approvedBuzzWords:
            finalArray.append(a[0])
        return finalArray

        #minOccurences=1
        #print(findBuzzWords("Google",minOccurences))

