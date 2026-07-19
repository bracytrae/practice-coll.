import java.util.Scanner;

public class FiveDigitIdValidator {
    public static void main (String [] args) {
        Scanner input = new Scanner(System.in);

        // This makes it so that so the program allows the user to test ID's until they enter -1
        while (true) {

            // Reads for the ID number, but constraints for receiving the ID number are included below.
            System.out.print("Please enter a five-digit ID (-1 to end): ");
            int ID = input.nextInt();

            // If -1 is entered the program stops.
            if (ID == -1) {
                System.out.println("Program Terminated!.");
                break;
            }

            // If the ID is a negative number.
            if (ID < 0) {
                System.out.println("Invalid ID, it must be a positive number!");
                continue;
            }

            // If the ID contains more or less of 5 digits.
            if (ID < 10000 || ID > 99999) {
                System.out.println("Invalid ID, it must be 5 digits!");
                continue;
            }

            // The CheckDigit is the number contained in the one's place so the last digit.
            int CheckDigit = ID % 10;

            // The FourDigit is the ID divided by 10 which account only for the first 4 digits of the inputted ID.
            int FourDigits = ID / 10;

            // Digit1 extracts the thousands digit.
            int Digit1 = FourDigits / 1000;

            // Digit 2 extracts the hundreds digit.
            int Digit2 = (FourDigits / 100) % 10;

            // Digit 3 extracts the tens digit.
            int Digit3 = (FourDigits / 10) % 10;

            // Digit 4 extracts the ones digit.
            int Digit4 = FourDigits % 10;

            // The total sum of the 4 digits.
            int Sum = Digit1 + Digit2 + Digit3 + Digit4;

            // The Remainder of the Sum % 6.
            int Remainder = Sum % 6;

            if (Remainder == CheckDigit) {
                System.out.println("Valid ID!");
            } else {
                System.out.println("Error Includes Incorrect Check Digit!");
            }
        }

        input.close();
    }
}
