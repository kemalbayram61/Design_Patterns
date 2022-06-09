public class VictorianRoom implements Room{
    private Chair chair;
    private Sofa sofa;
    private Table table;
    public VictorianRoom(){
        this.chair = new VictorianChair();
        this.sofa  = new VictorianSofa();
        this.table = new VictorianTable();
    }
    @Override
    public void listRoomBelongings() {
        System.out.println(this.chair.toString());
        System.out.println(this.sofa.toString());
        System.out.println(this.table.toString());
    }
}
