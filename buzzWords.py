import re
import wikipedia
class BuzzWords:
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
        content = wikipedia.page(wikipedia.search(name)[0]).content
        return content

    def findBuzzWords(self,name,k):
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

