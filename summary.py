import wikipedia

class Summary:
    def getSummary(self,name):
        try:
            s=wikipedia.summary(name, sentences=2)
            return s
        except wikipedia.exceptions.DisambiguationError as ex:
            s=wikipedia.summary(ex.args[1][0],sentences=2)
            return s

