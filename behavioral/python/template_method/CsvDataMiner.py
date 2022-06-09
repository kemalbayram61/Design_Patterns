from DataMinerA import DataMiner

class CSVDataMiner(DataMiner):
    def openFile(self, path: str) ->str:
        return "File.csv"
    def extractData(self, file: str) ->str:
        return "aaaaaaaaaaa..."
    def parseData(self, data: str) ->str:
        return  "a.a.a.a.a..."
    def analyzeData(self, data: str) ->str:
        return "1.0.1.0.0.1.1..."
    def sendReport(self, data: str) ->None:
        print("CSV report sent.")
    def closeFile(self, file: str) ->None:
        print("CSV file closed.")