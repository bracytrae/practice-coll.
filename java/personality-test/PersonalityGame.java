import java.util.Scanner; // import for Scanner (reads user input).
import java.util.function.Consumer; // import for lambdas (lets you write functional logic in fewer lines).

enum Personality { // enums (named constants that are type-safe, there type is literally Personality, with a fixed set of constants, & the compiler forces type safety!).
    EXPLORER,
    STRATEGIST,
    CREATOR,
}

public class PersonalityGame {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); // Scanner is declared and named input.

        // int counter variables named explorer, strategist, & creator, to keep track fo the user's stats.
        int explorer = 0;
        int strategist = 0;
        int creator = 0;

        System.out.println("Welcome to the Personality Analyzer Game!");
        System.out.println("--you are given cool scenarios to choose from--\n");

        // scenarios inside a variable type string that makes them intuitive and easier to handle.
        String scenario1 =
                "Scenario 1:\n\n" +
                        "You wake up in a mysterious forest. What do you do?\n\n" +
                        "1 - Walk around and explore\n" +
                        "2 - Look for a safe place to plan\n" +
                        "3 - Gather materials and build tools\n" +
                        "Choice: ";

        System.out.print(scenario1); // scenario1 printed out from its type string var.
        int choice = input.nextInt(); // intakes an integer from a selected choice.

        switch(choice) { // if the integer matches a particular case it increments counter variables to update the user's stats.
            case 1 -> explorer++;
            case 2 -> strategist++;
            case 3 -> creator++;
            default -> System.out.println("Invalid Choice!");
        }

        // scenarios inside a variable type string that makes them intuitive and easier to handle.
        String scenario2 =
                "Scenario 2:\n\n" +
                        "You find an abandoned building. What do you do?\n\n" +
                        "1 - Search every room\n" +
                        "2 - Check exits and entrances first\n" +
                        "3 - Try to fix something broken inside\n" +
                        "Choice: ";

        System.out.print(scenario2); // scenario2 printed out from its type string var.
        choice = input.nextInt(); // no extra int needed, because it's type is technically already declared when reading from the first scenario.

        switch(choice) { // if the integer matches a particular case it increments counter variables to update the user's stats.
            case 1 -> explorer++;
            case 2 -> strategist++;
            case 3 -> creator++;
            default -> System.out.println("Invalid Choice!");
        }

        // scenarios inside a variable type string that makes them intuitive and easier to handle.
        String scenario3 =
                "Scenario 3:\n\n" +
                        "You meet a stranger. What do you do?\n\n" +
                        "1 - Ask them about the world\n" +
                        "2 - Ask about survival tips\n" +
                        "3 - Ask what they can build or create\n" +
                        "Choice: ";

        System.out.print(scenario3); // scenario3 printed out from its type string var.
        choice = input.nextInt(); // no extra int needed, because it's type is technically already declared when reading from the first scenario.

        switch(choice) { // if the integer matches a particular case it increments counter variables to update the user's stats.
            case 1 -> explorer++;
            case 2 -> strategist++;
            case 3 -> creator++;
            default -> System.out.println("Invalid Choice!");
        }

        // scenarios inside a variable type string that makes them intuitive and easier to handle.
        String scenario4 =
                "Scenario 4:\n\n" +
                        "You find strange technology. What do you do?\n\n" +
                        "1 - Test what it does\n" +
                        "2 - Analyze how it works first\n" +
                        "3 - Try modifying it\n" +
                        "Choice: ";

        System.out.print(scenario4); // scenario4 printed out from its type string var.
        choice = input.nextInt(); // no extra int needed, because it's type is technically already declared when reading from the first scenario.

        switch(choice) { // if the integer matches a particular case it increments counter variables to update the user's stats.
            case 1 -> explorer++;
            case 2 -> strategist++;
            case 3 -> creator++;
            default -> System.out.println("Invalid Choice!");
        }

        // determines the final personality type for the trait with the highest incremented score and stores it as result. (uses the special logical operator (AND (&&))
        Personality result;

        if (explorer >= strategist && explorer >= creator) {
            result = Personality.EXPLORER;
        } else if (strategist >= explorer && strategist >= creator) {
            result = Personality.STRATEGIST;
        } else {
            result = Personality.CREATOR;
        }

        // usage of Lambda to display the result
        Consumer<Personality> displayResult =
                trait -> System.out.println("\nYour personality type is: " + trait);

        displayResult.accept(result); // accepts the result so that it can be used in the Lambda expression above.

        // shows the total scores and how much they've incremented the personality type that should be displayed is that with the highest score which is what's incremented the most.
        System.out.println("\nFinal Scores:");
        System.out.println("Explorer: " + explorer);
        System.out.println("Strategist: " + strategist);
        System.out.println("Creator: " + creator);

        input.close();
    }
}

