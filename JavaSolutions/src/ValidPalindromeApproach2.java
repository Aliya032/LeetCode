public class ValidPalindromeApproach2 {
    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(isPalindrome("race a car"));
        System.out.println(isPalindrome("race car"));
        System.out.println(isPalindrome(" "));
        System.out.println(isPalindrome("0P"));
    }
    public static boolean isPalindrome(String s) {
        //initializing two pointers
        int leftIndex = 0;
        int rightIndex = s.length()-1;

        while (leftIndex < rightIndex) {
            //if the character at the left index is not alphanumeric, move the left pointer to the right
            if (!Character.isLetterOrDigit(s.charAt(leftIndex))) {
                leftIndex++;
            }
            //if the character at the right index is not alphanumeric, move the right pointer to the left
            else if (!Character.isLetterOrDigit(s.charAt(rightIndex))) {
                rightIndex--;
            }
            //if the characters at both indexes are alphanumeric, compare them ignoring case
            else if (Character.toLowerCase(s.charAt(leftIndex)) != Character.toLowerCase(s.charAt(rightIndex))) {
                //if characters do not match, it's not a palindrome
                return false;
            } else {
                //if characters match, move both pointers
                leftIndex++;
                rightIndex--;
            }
        }
        //if all alphanumeric characters were matched successfully it's a palindrome.
        return true;
    }
}
