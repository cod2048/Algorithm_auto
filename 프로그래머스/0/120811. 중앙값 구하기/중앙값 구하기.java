import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int arrayLen = array.length;
        Arrays.sort(array);
        int centerValue = arrayLen / 2;
        answer = array[centerValue];
        return answer;
    }
}