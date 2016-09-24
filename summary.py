import wikipedia

class Summary:
    def correctName(self,name):
        results = wikipedia.search(name,3)
        for result in results:
            try:
                for category in wikipedia.WikipediaPage(result).categories:
                    if "software" in category or "computer" in category:
                        return result
            except:
                True
    def getSummary(self,name):
        try:
            s=wikipedia.summary(self.correctName(self,name), sentences=2)
            return s
        except wikipedia.exceptions.DisambiguationError as ex:
            s=wikipedia.summary(ex.args[1][0],sentences=2)
            return s

