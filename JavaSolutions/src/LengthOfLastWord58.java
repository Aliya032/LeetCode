public class LengthOfLastWord58 {
    public static void main(String[] args) {
        System.out.println(lengthOfLastWord("Hello World"));
        System.out.println(lengthOfLastWord("   fly me   to   the moon  "));
        System.out.println(lengthOfLastWord("luffy is still joyboy"));
    };
    public static int lengthOfLastWord(String s) {
        String[] wordArray = s.split(" ");
        int count = 0;
        for(int i = 0; i<wordArray.length; i++) {
            if(i==wordArray.length-1) {
                for (int j = 0; j<wordArray[wordArray.length-1].length();j++) {
                    count++;
                }
            }
        }
        return count;
    };
}
