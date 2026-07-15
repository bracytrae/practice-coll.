#include <iostream>

// FizzBuzz practice:
// Print Fizz for multiples of 3, Buzz for multiples of 5,
// and FizzBuzz when a number is a multiple of both.

int main() {
    // Loop through each number from 1 to 15.
    for (int i = 1; i <= 15; i++) {
        // Check both numbers first so multiples of 15 print FizzBuzz.
        if (i % 3 == 0 && i % 5 == 0) {
            std::cout << "FizzBuzz" << std::endl;
        // Multiples of 3 print Fizz.
        } else if (i % 3 == 0) {
            std::cout << "Fizz" << std::endl;
        // Multiples of 5 print Buzz.
        } else if (i % 5 == 0) {
            std::cout << "Buzz" << std::endl;
        // Print the number when none of the conditions match.
        } else {
            std::cout << i << std::endl;
        }
    }
    return 0;
}
