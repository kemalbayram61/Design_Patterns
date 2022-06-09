public interface DataMiner {
    String openFile(String  path);

    String extractData(String file);

    String parseData(String data);

    String analyzeData(String data);

    void sendReport(String data);

    void closeFile(String file);
}
