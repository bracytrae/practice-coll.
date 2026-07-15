import java.util.Scanner; // imported the scanner class to read user input.

public class TaxBracket { // calculates a user's net pay (after taxes) based on their tax bracket

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); // created an object for the scanner class.

        System.out.print("Enter your first name: ");
        String FirstName = input.next(); // referenced the scanner class object.

        System.out.print("Enter your last name: ");
        String LastName = input.next(); // referenced the scanner class object.

        System.out.print("Enter Your Monthly Gross Pay: $");
        double GrossPay = input.nextDouble(); // referenced the scanner class object.

        System.out.print("Enter The Number Of Dependents: ");
        int Dependents = input.nextInt(); // referenced the scanner class object.

        input.close(); // closed the input so the program expects no further input.

        double TaxRate; // created a double variable type for TaxRate, the sequence determines a TaxRate via the num of Dependents.

            if (Dependents <= 1) { // 0-1 dependents
                TaxRate = 0.20;
            } else if (Dependents <= 3) { // 2-3 dependents
                TaxRate = 0.15;
            } else {
                TaxRate = 0.10; // 4+ dependents
            }

        double NetPay = GrossPay - (GrossPay * TaxRate); // NetPay is evaluated after the TaxRate sequence completes as a var w/ arithmetic equations.

        // A collection of print statements are established that print out the user's Name, Gross Pay, Dependents, Tax Rate, & Net Pay.

        System.out.println("\nName: " + FirstName + " " + LastName);
        System.out.println("Gross Pay: $" + GrossPay);
        System.out.println("Dependents: " + Dependents);
        System.out.println("Tax Rate: " + (int)(TaxRate * 100) + "%");
        System.out.println("Net Pay: " + "$" + NetPay);

    }
}



