public class Main
{
    public static void main(String[] args)
    {
        Session session = Session.getSession();
        System.out.println(session.getUserName() + session.getUserCode() + session.getUserType());
    }
}
