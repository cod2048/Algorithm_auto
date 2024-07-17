import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader scanner = new BufferedReader(new InputStreamReader(System.in));

        String[] numbers = scanner.readLine().split(" ");

        int[] array = Arrays.stream(numbers).mapToInt(Integer::parseInt).toArray();

        System.out.println(array[0] + array[1]);
    }
}