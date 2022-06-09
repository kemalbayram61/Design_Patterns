public class ModernRoom implements Room{
    private Chair chair;
    private Sofa sofa;
    private Table table;
    public ModernRoom(){
        this.chair = new ModernChair();
        this.sofa  = new ModernSofa();
        this.table = new ModernTable();
    }
    @Override
    public void listRoomBelongings() {
        System.out.println(this.chair.toString());
        System.out.println(this.sofa.toString());
        System.out.println(this.table.toString());
    }
}
