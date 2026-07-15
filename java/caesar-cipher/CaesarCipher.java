import java.util.Scanner;

public class CaesarCipher {

    // step 1 --> creates the encrypted method
    public static String encrypt(String text, int shift) {

        // step 2 --> creates the StringBuilder object
        StringBuilder result = new StringBuilder();

        // step 3 --> creates the for-each loop
        for (char character : text.toCharArray()) {

            // step 4 --> checks if the character is a letter
            if (Character.isLetter(character)) {

                // step 5 --> checks if the letter is uppercase or lowercase

                // (? :) the ternary operator provides either the a or A character depending on if the letter is upper case or lower case.
                char base = Character.isLowerCase(character) ? 'a' : 'A';

                /* step 6 --. where the shift happens depending on the user input

                because the characters are ASCII you can add or subtract them

                 */

                // the (char) type is what lets you convert the int result back into a character
                // the %26 prevents it going above 26, wrapping the shift back around and reiterating back to the beginning

                char shifted = (char) ((character - base + shift) % 26 + base);

                // step 7 --> append the shifted char to result (in other words it adds the shifted char to result.)
                result.append(shifted);

            } else {

                // step 8 --> if it's not a letter, it stays as is which could include (spaces, punctuation, numbers, etc...)
                result.append(character);
            }
        }

        // step 9: converts StringBuilder to String and return
        return result.toString();
    }

    public static void main(String[] args) {

        // step 10: add scanner
        Scanner scanner = new Scanner(System.in);

        // step 11: get user's text input
        System.out.print("Enter text to encrypt: ");
        String inputText = scanner.nextLine();

        // step 12: get user's shift input
        System.out.print("Enter shift key (0-25): ");
        int shiftKey = scanner.nextInt();

        // step 13: encrypt and print result
        String encrypted = encrypt(inputText, shiftKey);
        System.out.println("Encrypted text: " + encrypted);

        scanner.close();

        /*
        The key insight is that regular Strings in Java are immutable — once created, they can never be changed. So if you wrote result = result + shifted inside the loop, Java would silently throw away the old string and create a brand new one on every single iteration. For a short message that's fine, but for anything long it wastes a lot of memory.

        StringBuilder solves this by giving you a single mutable object that just grows as you call .append() on it. You build up the whole encrypted message inside it, and only at the very end does .toString() convert it into a regular String to return.

         */

    }
}