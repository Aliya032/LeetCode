public class RansomNote383 {
    public static void main(String[] args) {
        System.out.println(canConstruct("a", "b"));
        System.out.println(canConstruct("aa", "ab"));
        System.out.println(canConstruct("aa", "aab"));
        System.out.println(canConstruct("cab", "abcab"));
        System.out.println(canConstruct("cab", "abab"));
    }

    public static boolean canConstruct(String ransomNote, String magazine) {
        int[] chars = new int[26];

        for (char c: magazine.toCharArray()) {
            chars[c - 'a']++;
        }

        for (char c: ransomNote.toCharArray()) {
            if (chars[c - 'a'] == 0) {
                return false;
            }
            chars[c - 'a']--;
        }
        return true;
    }
}

/*
class Solution{
    public static boolean canConstruct(String ransomNote, String magazine) {
        int[] chars = new int[26];

        for (char c: magazine.toCharArray()) {
            chars[c - 'a']++;
        }

        for (char c: ransomNote.toCharArray()) {
            if (chars[c - 'a'] == 0) {
                return false;
            }
            chars[c - 'a']--;
        }
        return true;
    }
}
*/

