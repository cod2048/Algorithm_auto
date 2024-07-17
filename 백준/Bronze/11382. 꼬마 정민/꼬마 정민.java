import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] s = bufferedReader.readLine().split(" ");

        long[] array = Arrays.stream(s).mapToLong(Long::parseLong).toArray();

        System.out.println(array[0] + array[1] + array[2]);
    }
}