#include <iostream> // for reading user input and output, given "io".
#include <string> // helps C++ know what a string object is, so it can be declared and used within the program/memory and functions are special and declarable specific to the string object created.

int main() {

    std::cout << "===================\nPassword Checker 🔐\n===================\n";

    std::string password; // string object password is created. 

    bool validPassword = false; // created a boolean validPassword so that if the user enters in an incorrect password it prompts the user to enter in a password again which just reinforced the validity of the program.

    // valid password sequence 
    while (!validPassword) {


        bool hasNumber = false; // a boolean for whether or not the password contains a number is created for the sequences.
        bool hasSpecial = false; // a boolean for whether or not the password contains a special character is created for the sequences. 

        std::cout << "\nEnter a password: "; // prompts the user to enter in a password. 
       
        getline(std::cin, password); // this reads the entire line of input by the user.

        // loops through the length of the password that's been stored in memory and uses the .length() method specific to the that string objects class.
        for (int i = 0; i < password.length(); i++) {

            // checks for numbers 0-9.
            if (password[i] >= '0' && password[i] <= '9') {
                hasNumber = true;
            }

            // checks if any special characters exist.
            else if (
                password[i] == '!' ||
                password[i] == '@' ||
                password[i] == '#' ||
                password[i] == '$' ||
                password[i] == '%'
            ) {
                hasSpecial = true;
            }
        }

        // password validity sequence 
        if (password.length() < 8) {
            std::cout << "❌ Password must be at least 8 characters.\n";
        }
        else if (!hasNumber) { // if it does not contain a number 0-9.
            std::cout << "❌ Password must include a number.\n";
        }
        else if (!hasSpecial) { // if it does not contain a special character. 
            std::cout << "❌ Password must include a special character.\n";
        }
        else {
            validPassword = true; 
            std::cout << "✅ Valid password!\n";
        }
    }

    std::cout << "\nPassword Checker 🔐 Program Terminated...";

    // this prints if the password is a valid password.
    
}
