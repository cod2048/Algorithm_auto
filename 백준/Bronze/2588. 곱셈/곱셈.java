import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int num1 = Integer.parseInt(bufferedReader.readLine());
        String num2 = bufferedReader.readLine();

        int digit1 = Character.getNumericValue(num2.charAt(2));
        int digit2 = Character.getNumericValue(num2.charAt(1));
        int digit3 = Character.getNumericValue(num2.charAt(0));

        System.out.println(num1 * digit1);
        System.out.println(num1 * digit2);
        System.out.println(num1 * digit3);

        int num2Int = Integer.parseInt(num2);
        System.out.println(num1 * num2Int);

    }
}