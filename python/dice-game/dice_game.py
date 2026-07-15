# program only uses conditional statements & nested loops

# imports random for dice roll
import random

# welcoming prompts
print("Welcome to the Eight-Sided Dice Game.")

print("\nYou are given $500 to start"
      "\nYou can't play once you run out of money.")

# constant values defined including user balance and boolean values that help with properly exiting the loops given the conditions
player_balance = 500
dice_game = True

# user has a balance and continue playing is Y or y
while player_balance > 0 and dice_game:

    # prompt's value resets when it exits the loop so that the loop can be accessed again
    prompt = True

    # prompts for the user's bet amount
    bet_amount = int(input("\nEnter the amount you want to bet:"))


    # bet amount is less than or equal to user balance
    if bet_amount <= player_balance:

        # dice system
        die_1 = random.randint(1, 8)
        die_2 = random.randint(1, 8)

        # dice sum
        dice_sum = die_1 + die_2

        # guess of dice sum
        dice_sum_guess = int(input("Guess the dice sum:"))

        # guess of dice sum is within the range of 2 - 12
        if dice_sum_guess < 2 or dice_sum_guess > 12:
            print("You Have To Bet Within The Dice Range!")

        # guess of dice sum is not equal to dice sum
        elif dice_sum_guess != dice_sum:
            player_balance -= bet_amount
            print("\nYou guessed the dice sum incorrectly!")
            print("Balance:", player_balance)

        # guess of dice sum is equal to dice sum, the dice are not equal to one another
        elif dice_sum_guess == dice_sum and die_1 != die_2:
            player_balance += bet_amount
            print("\nYou guessed the dice sum correctly but the die do not equal one another!")
            print("Balance:", player_balance)

        # guess of dice sum is equal to dice sum, dice are equal to one another
        elif dice_sum_guess == dice_sum and die_1 == die_2:
            player_balance += bet_amount * 2
            print("\nYou guessed the dice sum correctly and the die equal one another!")
            print("Balance:", player_balance)

        # user wishes to continue or discontinue the game
        while prompt:
            continue_playing = input("\nDo you want to continue playing? (Y, y, N, n):")

            if continue_playing in ['Y', 'y', 'N', 'n']:

                if continue_playing in ['Y', 'y']:
                    prompt = False

                elif continue_playing in ['N', 'n']:
                    prompt = False
                    dice_game = False

            else:
                print("Enter a valid input!")

    # bet amount is 0 or negative or more than user balance
    elif bet_amount < 0 or bet_amount > player_balance:
        print("Bet amount can't be above or equal to or lower than your balance!")

# if the user wishes to discontinue or the user has no balance

else:

    print("You have no balance, thank you so much for playing!")


