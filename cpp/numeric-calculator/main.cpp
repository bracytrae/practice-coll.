#include <iostream> // for user input via "cin" = character input, and user output, via "cout" character output.
#include <iomanip> // for formatting, helps give control of decimal places output.

int main() {


    // created variables.
    char op;
    double num1, num2;
    char choice;

    // "std" = standard name space folder, (cout, cin, string, vector, endl).

    // formats decimal output to 2 decimal places.
    std::cout << std::fixed << std::setprecision(2);

    // do-while, which helps with prompting the user on whether they wish to continue the program.
    do {

        // asks user for operator
        std::cout << "Enter an operator (+, -, *, /): ";
        std::cin >> op; // stores it as "op" = operator.

        // asks user for numbers
        std::cout << "Enter two numbers: ";

        // validates number inputs, if number inputs are different then the specified variables by use of the standard name space folder toward the top of the program this branch executes.
        if (!(std::cin >> num1 >> num2)) {

            std::cout << "Error: Invalid number input!\n";
            return 1; // the program unsuccessfully closes so an error/failure occurs within the calculator program.
        }

        // performs calculation's based on inputted operator w/ the use of switch case.
        switch (op) {

            case '+':

                std::cout << "\nResult: "
                          << num1 << " + " << num2
                          << " = " << (num1 + num2);

                break;

            case '-':

                std::cout << "\nResult: "
                          << num1 << " - " << num2
                          << " = " << (num1 - num2);

                break;

            case '*':

                std::cout << "\nResult: "
                          << num1 << " * " << num2
                          << " = " << (num1 * num2);

                break;

            case '/':

                // prevents division by zero
                if (num2 != 0) {

                    std::cout << "\nResult: "
                              << num1 << " / " << num2
                              << " = " << (num1 / num2);
                }

                else {

                    std::cout << "\nError: Cannot divide by zero!";
                }

                break;

            default: // if the "char" op, does not match any of the cases the default case executes to print out that an invalid operator has been printed.

                std::cout << "\nError: Invalid operator!";
        }

        // asks the user if they wish to continue with the program.
        std::cout << "\n\nWould you like to calculate again? (y/n): ";
        std::cin >> choice;

    } while (choice == 'y' || choice == 'Y');

    std::cout << "\nCalculator closed.\n";

    return 0; // the program successfully closes.

}
