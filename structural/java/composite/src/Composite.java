import java.util.ArrayList;

public class Composite extends Component {

    private ArrayList<Component> children;

    public Composite(){
        this.children = new ArrayList<>();
    }

    @Override
    public void add(Component component) {
        this.children.add(component);
        component.setParent(this);
    }

    @Override
    public void remove(Component component) {
        this.children.remove(component);
        component.setParent(null);
    }

    @Override
    public String operation() {
        ArrayList<String> result = new ArrayList<>();
        for(Component component: this.children){
            result.add(component.operation());
        }
        return "Branch(" + String.join("+", result) + ')';
    }

    public boolean isComposite(){
        return true;
    }
}
