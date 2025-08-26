class Solution {
    public int[] solution(int n, long left, long right) {
        int len = (int) (right - left + 1);
        int[] answer = new int[len];
        
        for (int i=0;i < len; i++) {
            long k = left + i;
            int x = (int) (k / n);
            int y = (int) (k % n);
            answer[i] = Math.max(x, y) + 1;
        }
        return answer;
    }
}