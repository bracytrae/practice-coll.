// FizzBuzz practice:
// Print Fizz for multiples of 3, Buzz for multiples of 5,
// and FizzBuzz when a number is a multiple of both.

// Loop through each number from 1 to 15.
for (let i = 1; i <= 15; i++){
    // Check both numbers first so multiples of 15 print FizzBuzz.
    if (i % 3 === 0 && i % 5 === 0){
        console.log("FizzBuzz");
    // Multiples of 3 print Fizz.
    } else if (i % 3 === 0){
        console.log("Fizz");
    // Multiples of 5 print Buzz.
    } else if (i % 5 === 0){
        console.log("Buzz");
    // Print the number when none of the conditions match.
    } else {
        console.log(i);
    }
}

