import java.util.ArrayList;
import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        List<DataMiner> dataMiners = new ArrayList<>();
        dataMiners.add(new CSVDataMiner());
        dataMiners.add(new JSONDataMiner());
        dataMiners.add(new PDFDataMiner());

        dataMiners.forEach(miner ->
        {
            String file      = miner.openFile("yyyy/xxxx");
            String exData    = miner.extractData(file);
            String parseData = miner.parseData(exData);
            String analysis  = miner.analyzeData(parseData);
            miner.sendReport(analysis);
            miner.closeFile(file);
        });
    }
}
