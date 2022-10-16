public class Main {

    public static void clientCode(Component component){
        System.out.println("Result:" + component.operation());
    }

    public static void clientCode2(Component component1, Component component2){
        if(component1.isComposite()) component1.add(component2);
        System.out.println("Result:" + component1.operation());
    }

    public static void main(String [] args){
        Leaf simple = new Leaf();
        System.out.println("Client: I've got a simple component:");
        clientCode(simple);

        Composite tree = new Composite();
        Composite branch1 = new Composite();
        Composite branch2 = new Composite();

        branch1.add(new Leaf());
        branch1.add(new Leaf());

        branch2.add(new Leaf());

        tree.add(branch1);
        tree.add(branch2);

        System.out.println("Client: Now I've got a composite tree:");
        clientCode(tree);

        System.out.println("Client: I don't need to check the components classes even when managing the tree:");
        clientCode2(tree, simple);
    }
}
