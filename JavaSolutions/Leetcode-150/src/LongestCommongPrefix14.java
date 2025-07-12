import java.util.Arrays;

/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 */
public class LongestCommongPrefix14 {
    public static void main(String[] args) {
        String[] arrays = {"flower","flow","flight"};
        System.out.println(longestCommonPrefix(arrays));
        String[] arrays2 = {"dog","racecar","car"};
        System.out.println(longestCommonPrefix(arrays2));
    }
    public static String longestCommonPrefix(String[] strs) {
        //sorting the array
        Arrays.sort(strs);

        //selecting first and last array element
        String firstElement = strs[0];
        String lastElement = strs[strs.length-1];

        //fining the minimum element
        int minElementLength = Math.min(firstElement.length(), lastElement.length());

        //checking if the first characters are same
        int i  = 0;
        while (i< minElementLength && (firstElement.charAt(i) == lastElement.charAt(i))) {
            i++;
        }
        return firstElement.substring(0,i);
    }

}
