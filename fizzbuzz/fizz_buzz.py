# FizzBuzz practice:
# Print Fizz for multiples of 3, Buzz for multiples of 5,
# and FizzBuzz when a number is a multiple of both.

# Loop through each number from 1 to 15.
for number in range(1, 16):
    # Check both numbers first so multiples of 15 print FizzBuzz.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Multiples of 3 print Fizz.
    elif number % 3 == 0:
        print("Fizz")
    # Multiples of 5 print Buzz.
    elif number % 5 == 0:
        print("Buzz")
    # Print the number when none of the conditions match.
    else:
        print(number)
