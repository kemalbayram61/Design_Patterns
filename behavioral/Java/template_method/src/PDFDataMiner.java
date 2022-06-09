public class PDFDataMiner implements DataMiner{
    @Override
    public String openFile(String path) {
        return "file.pdf";
    }

    @Override
    public String extractData(String file) {
        return "aaaaaaaaaaa...";
    }

    @Override
    public String parseData(String data) {
        return  "a.a.a.a.a...";
    }

    @Override
    public String analyzeData(String data) {
        return "1.0.1.0.0.1.1...";
    }

    @Override
    public void sendReport(String data) {
        System.out.println("PDF report sent.");
    }

    @Override
    public void closeFile(String file) {
        System.out.println("PDF file closed.");
    }
}
