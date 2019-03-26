import java.net.*;

public class Main
{
    public static void main(String[] args)
    {
        try
        {
            final var server_address = "220.69.240.146";
            final var port = 12345;
            var socket = new Socket(server_address, port);
            var writer = socket.getOutputStream();
            writer.write("hello?".getBytes("UTF-8"));
            socket.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }
}
