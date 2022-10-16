abstract class Component {
    private Component parent;

    public Component(){
        this.parent = null;
    }

    public Component getParent(){
        return this.parent;
    }

    public void setParent(Component parent){
        this.parent = parent;
    }

    public boolean isComposite(){
        return false;
    }

    public abstract void add(Component component);

    public abstract void remove(Component component);

    public abstract String operation();
}
