import java.util.Scanner; // imported Scanner --> used to read user input...

public class WordGuesser { 

    /*
    
    just some quick personal reminders on how statements can be declared and operate.
    
    public; (anyone can access this method.)
    static; (it belongs to the class itself, not an object, so Java can run it without creating an object first.)
    void; (it doesn't return anything.)
    main; (the name the JVM looks for when starting your program.)
    JVM = "Java Virtual Machine."
    
    \*

    // code that makes all of this work below --> 
    
    public static void main(String[] args) {

        // defining the scanner, to intake input.
        Scanner input = new Scanner(System.in); 

        // defining a boolean to validate whether or not the user chooses to continue playing.
        boolean playAgain = true; 

        // use of the boolean.
        while (playAgain) { 

            // the secret word that the user must input.
            String secretWord = "java"; 
            
            // the number of attempts the user gets.
            int attempts = 5; 

            // just a simple welcoming message...
            System.out.println("Welcome to the Word Guesser Game!"); 

            // when the amount of attempts is greater than 0...
            while (attempts > 0) { 

                // gives the user feedback on how many attempts they have & how many remain.
                System.out.println("You have" + " " + attempts + " " + "attempts to guess the secret word."); 

                // user input.
                System.out.print(">> "); 

                // user input picked up as var guess w/ the type being a String (non-primitive).
                String guess = input.nextLine(); 

                // use .equals() instead of == to compare the values, given that the String is a non-primitive.
                if (guess.equals(secretWord)) { 

                    // prints out correct if the guess is equal to the secretWord (camel-case Java typing convention) & prompts the user to enter p/P or anything other than this to stop the game.
                    System.out.println("Correct! Input [p] to play again or Input [something] to stop."); 

                    // reads the response of the user.
                    String response = input.nextLine(); 

                    // if the response is P/p, it breaks out of the current loop and goes back out to the while (playAgain) loop.
                    if (response.equalsIgnoreCase("p")) { 
                        
                        break;
                        
                    // if the response is anything other than P/p, it stops the program.
                    } else { 
                        
                        playAgain = false;
                        break;
                        
                    }

                // if the response does not equal the secret word, it "post" decrements the number of attempts, so it decrements after the validation sequence occurs and prints out "Incorrect".
                } else { 
                    
                    attempts--;
                    System.out.println("Incorrect!");
                    
                }
            }

            // when the attempts are not greater than 0 but equal to, this "catches" that
            if (attempts > 0) { 

                // prompts the user to play again.
                System.out.println("Out of attempts! Press [p] to play again"); 

                // catches the input as "response".
                String response = input.nextLine(); 

                // if the response does not equal p, then the game ends.
                // value can be thought of as true, !value can be thought of as false, when the response is false in being p the game does not continue.
                if (!response.equalsIgnoreCase("p")) { 
                    playAgain = false;
                }
            }
        }
    
        // closes the Scanner used when the program halts. The Scanner used at the beginning of the code is named input, which is a name conventionally used for imported Scanners used to read user input. 
        input.close(); 
    
    }
}

