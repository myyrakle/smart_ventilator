//앱에서, 서버로부터 받는 Json 데이터 규격입니다.
//Java Gson 사용을 위해 구현되었습니다.

public class JsonFromPi
{
    String command;
    JsonSensingType current;
    JsonDatasType[] datas;
    boolean fan_on;
}