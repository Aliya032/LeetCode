import java.util.HashSet;
import java.util.Set;

public class LongestSubstringWithoutRepeatingCharacters3 {
    public static void main(String[] args) {
        String s1 = "abcabcbb";
        String s2 = "bbbbb";
        String s3 = "pwwkew";
        System.out.println(lengthOfLongestSubstring(s1));
        System.out.println(lengthOfLongestSubstring(s2));
        System.out.println(lengthOfLongestSubstring(s3));
    }
    public static int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }

        int finalLength = Integer.MIN_VALUE;
        Set <Character> set = new HashSet<>();
        int l = 0;
        for (int r = 0; r <s.length(); r++) {
            if (set.contains(s.charAt(r))){
                while (l < r && set.contains(s.charAt(r))) {
                    set.remove(s.charAt(l));
                    l++;
                }
            }
            set.add(s.charAt(r));
            finalLength = Math.max(finalLength, (r-l+1));
        }
        return finalLength;
    }
}
