import java.util.Scanner;

public class TriangleMethods {

    // public allows access to all other classes,
    // static main function is called without creating an object
    // void no return value is needed
    // main is the name of the function
    // String[] args is for any command line arguments used.


    public static void main(String[] args) {

        // contains the returned result so that if the result is equal to 0 it prints out that an Error occurs.
        double result = triangleType();

        if (result == 0) {
            System.out.println("Error: The measurements do not form a Triangle.");

        }
    }

    public static double triangleType() {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter Side 1 Of A Triangle: ");
        double triSide1 = input.nextDouble();

        System.out.print("Enter Side 2 Of A Triangle: ");
        double triSide2 = input.nextDouble();

        System.out.print("Enter Side 3 Of A Triangle: ");
        double triSide3 = input.nextDouble();

        // Sequence that checks for the Triangles validity.

        // all sides must be non-negative and not zero to form a valid triangle.

        if (triSide1 > 0 && triSide2 > 0 && triSide3 > 0 &&
                triSide1 + triSide2 > triSide3 &&
                triSide1 + triSide3 > triSide2 &&
                triSide2 + triSide3 > triSide1) {

            String triType;

            // All equal sides
            if (triSide1 == triSide2 && triSide2 == triSide3) {
                triType = "Equilateral";

            // Two equal sides
            } else if (triSide1 == triSide2 || triSide1 == triSide3 || triSide2 == triSide3) {
                triType = "Isosceles";

            // All unequal sides
            } else {
                triType = "Scalene";
            }

            // Add's the three side's of the inputted triangle.
            double triPerimeter = triSide1 + triSide2 + triSide3;

            // Find's the semiPerimeter which is known as 's' in geometry.
            double triSemiPerimeter = triPerimeter / 2.0;

            // Used Heron's formula, using the semi-perimeter and the Math.sqrt() method.
            double triArea = Math.sqrt(triSemiPerimeter * (triSemiPerimeter - triSide1) * (triSemiPerimeter - triSide2) * (triSemiPerimeter - triSide3));

            System.out.println("Triangle Type: " + triType);
            System.out.println("Triangle Perimeter: " + String.format("%.2f", triPerimeter));
            System.out.println("Triangle Area: " + String.format("%.2f", triArea));

        } else {
            return 0;
        }
        return 1; // returned 1 because void is not referenced as a return type in the triangleType method.
    }
}

// chaining and compound boolean expression

