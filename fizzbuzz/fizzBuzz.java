// FizzBuzz practice:
// Print Fizz for multiples of 3, Buzz for multiples of 5,
// and FizzBuzz when a number is a multiple of both.

public class fizzBuzz {
    public static void main(String[] args) {
        // Loop through each number from 1 to 15.
        for (int i = 1; i <= 15; i++) {
            // Check both numbers first so multiples of 15 print FizzBuzz.
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            // Multiples of 3 print Fizz.
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            // Multiples of 5 print Buzz.
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            // Print the number when none of the conditions match.
            } else {
                System.out.println(i);
            }
        }
    }
}
