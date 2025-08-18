import java.util.*;

class Solution {
    private static final Map<Character, Character> charMap = Map.of(
        ')','(',
        ']','[',
        '}','{'
    );

    public int solution(String s) {
        int n = s.length();
        if (n % 2 != 0) return 0;

        int ans = 0;
        for (int move = 0; move < n; move++) {
            if (isValidRotation(s, move)) ans++;
        }
        return ans;
    }

    private boolean isValidRotation(String s, int move) {
        int n = s.length();
        Deque<Character> stack = new ArrayDeque<>(n);

        for (int i = 0; i < n; i++) {
            char c = s.charAt((i + move) % n);

            if (charMap.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != charMap.get(c)) return false;
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
