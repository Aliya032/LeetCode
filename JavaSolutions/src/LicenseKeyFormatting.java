import java.sql.Ref;

public class LicenseKeyFormatting {
    public static void main(String[] args) {
        String s = "5F3Z-2e-9-w";
        int K = 4;
        String s2 = "2-5g-3-J";
        int p = 2;
        System.out.println(ReformatString(s,K));
        System.out.println(ReformatString(s2,p));

    }
    public static String ReformatString(String S, int k) {
        String temp = "";
        int length = S.length();
        for (int i = 0; i < length; i++) {
            if (S.charAt(i)!= '-') {
                temp += (Character.toUpperCase(S.charAt(i)));
            }
        }

        int lengthCaps = temp.length();

        String ans = "";
        int value = k;

        //iterating over the string from left to right pushing characters at an interval of k
        for (int i = lengthCaps-1; i>=0; i--) {
            if (value ==0) {
                value = k;
                ans += '-';
            }
            ans += temp.charAt(i);
            value--;
        }

        //reversing the ans so that
        char[] charArray = ans.toCharArray();
        reverse(charArray, charArray.length);
        String finalString = new String(charArray);
        return finalString;

    }

    static void reverse (char charArrayP[], int lengthCharArrayP) {
        char letter;
        for (int i = 0; i< lengthCharArrayP/2; i++) {
            letter = charArrayP[i];
            charArrayP[i] = charArrayP[lengthCharArrayP - i - 1];
            charArrayP[lengthCharArrayP - i - 1] = letter;
        }
    }
}
