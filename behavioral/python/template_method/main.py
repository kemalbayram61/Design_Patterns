from DocDataMiner  import DocDataMiner
from CsvDataMiner  import CSVDataMiner
from JsonDataMiner import JSONDataMiner
from DataMinerA    import DataMiner

if __name__ == "__main__":
    dataMiners: list[DataMiner] = []
    dataMiners.append(DocDataMiner())
    dataMiners.append(JSONDataMiner())
    dataMiners.append(CSVDataMiner())

    for miner in dataMiners:
        file:       str = miner.openFile("yyyy/xxxx")
        exData:    str = miner.extractData(file)
        parseData: str = miner.parseData(exData)
        analysis:  str = miner.analyzeData(parseData)
        miner.sendReport(analysis)
        miner.closeFile(file)