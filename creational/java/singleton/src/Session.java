public class Session
{
    private final String userName;
    private final String userCode;
    private final String userType;

    private final static Session session = new Session();

    private Session()
    {
        System.out.println("Session oluşturuluyor...");
        this.userCode = "001";
        this.userName = "testUser";
        this.userType = "Admin";
        System.out.println("Session oluşturuldu...");
    }

    public static Session getSession()
    {
        return session;
    }

    public String getUserName()
    {
        return this.userName;
    }

    public String getUserCode()
    {
        return this.userCode;
    }

    public String getUserType()
    {
        return this.userType;
    }
}