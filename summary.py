import wikipedia

class Summary:
    def getSummary(self,name):
        try:
            s=wikipedia.summary(name, sentences=2)
            return s
        except:
            return "Company not found"

