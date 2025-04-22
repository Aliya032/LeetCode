public class ValidPalidrome125 {
    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(isPalindrome("race a car"));
        System.out.println(isPalindrome(" "));
        System.out.println(isPalindrome("0P"));//it fails for this one.
    }
    public static boolean isPalindrome(String s) {
        String originalString = s;
        String result = s.replaceAll("[^a-zA-Z]", "").toLowerCase();
        System.out.println("original string: "+ s + " after replacing alphanumberic characters: "+ result);
        int i = 0;
        int j = result.length()-1;
        while (i < j) {
            if (result.charAt(i) != result.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
