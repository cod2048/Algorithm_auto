class Solution {
    public long solution(int num1, int num2) {
        double tmp = (double) num1/num2;
        long answer = (long) (tmp*1000);
        return answer;
    }
}