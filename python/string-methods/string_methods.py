def main():

    print("")

    print("Welcome To String Functions, Select A String Function From The List Given!\n")

    print(f"{'-' * 10}Menu{'-' * 10}")

    print(f"{'1. upper':<17}{'6. lower':<17}\n"
          f"{'2. strip':<17}{'7. replace':<17}\n"
          f"{'3. split':<17}{'8. join':<17}\n"
          f"{'4. find':<17}{'9. count':<17}\n"
          f"{'5. capitalize':<17}{'10. title':<17}")

    print("")

    choice()

def choice():

    user_choice =  input("Function: ")

    while not (user_choice.isdigit() and 1 <= int(user_choice) <= 10):
        print("\nInvalid Input, please choose a choice within range of 1 & 10!")
        user_choice = (input("Function: "))

    user_choice = int(user_choice)

    # proper implementation of switch case.

    if user_choice == 1:
        upper()
    elif user_choice == 2:
        strip()
    elif user_choice == 3:
        split()
    elif user_choice == 4:
        find()
    elif user_choice == 5:
        capitalize()
    elif user_choice == 6:
        lower()
    elif user_choice == 7:
        replace()
    elif user_choice == 8:
        join()
    elif user_choice == 9:
        count()
    elif user_choice == 10:
        title()

def string_universal_value():

    input_of_string = input("\nEnter A String: ")

    while input_of_string.isnumeric():
       print("Invalid Input, please choose a non-numerical value!")
       input_of_string = input("\nEnter A String: ")

    return input_of_string

def upper(): # Takes in one string value

    print("\nThe upper() function returns a string where all characters are uppercase.")
    upper_string_value = string_universal_value().upper()
    print(f"\nString Output: {upper_string_value}")

def strip(): # Takes in one string value

    print("\nThe strip() function removes any leading, and trailing whitespaces.")
    strip_string_value = string_universal_value().strip()
    print(f"\nString Output: {strip_string_value}")

def split(): # Takes in one string value

    print("\nThe split() function splits a string into a list.")
    split_string_value = string_universal_value().split()
    print(f"\nString Output: {split_string_value}")

def find(): # Takes in two string values

    print("\nThe find() function finds the first occurrence of a specified string (index).")

    reference = string_universal_value()
    find_value = input("\nEnter A String Value Contained Within The Previous String To Find It's First Occurrence (case sensitive): ")
    find_string_value = reference.find(find_value)
    print(f"\nString Output: {find_string_value}")

def capitalize(): # Takes in one string value

    print("\nThe capitalize() function capitalizes the first letter within a string.")
    capitalize_string_value = string_universal_value().capitalize()
    print(f"\nString Output: {capitalize_string_value}")

def lower(): # Takes in one string value

    print("\nThe lower() function returns a string where all characters are lowercase.")
    lower_string_value = string_universal_value().lower()
    print(f"\nString Output: {lower_string_value}")

def replace(): # Takes in 3 string values

    print("\nThe replace() function replaces a string with a string that is specified.")
    reference = string_universal_value()
    string_uni_sub_value = input("\nEnter A String Value Contained Within The Previous String You Wish To Replace (case sensitive): ")
    replace_value = input("\nEnter A String You Want To Replace The String With: ")
    replace_string_value = reference.replace(string_uni_sub_value, replace_value)
    print(f"\nString Output: {replace_string_value}")

def join(): # Takes in 2 string values

    print("\nThe join() function concatenates or joins elements of a iterable via a seperator value.")
    reference = string_universal_value()
    join_value = input("\nEnter A Seperator Value: ")
    join_string_value = join_value.join(reference)
    print(f"\nString Output: {join_string_value}")


def count(): # Takes in two string values

    print("\nThe count() function returns the # of occurrences of a specified string value within a string.")
    reference = string_universal_value()
    count_value = input("\nEnter A String Value Contained Within The Previous String To Find its # of occurrences (case sensitive): ")
    count_string_value = reference.count(count_value)
    print(f"\nString Output: {count_string_value}")

def title(): # Takes in one string value

    print("\nThe title() function returns a string where the first letter in every word is uppercased.")
    title_string_value = string_universal_value().title()
    print(f"\nString Output: {title_string_value}")

if __name__ == '__main__':
    main()

