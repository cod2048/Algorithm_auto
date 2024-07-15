class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n == 1) {
            return 0;
        } else if (n == 2 || n == 3) {
            return 2;
        } else {
            for (int i = 2; i <= n; i += 2) {
                answer += i;
            }
        }
        return answer;
    }
}