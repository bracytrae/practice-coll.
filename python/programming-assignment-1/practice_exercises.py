# Programming Assignment 1
import math

# What is your name:
name = input("What is your name?")

print("Hello " + name)

# How old are you:
age = int(input("How old are you?"))

future_age = age + 5

print("In 5 years you will be:", future_age)

# Entering A Two-Digit Number To Find The Sum:
couple_number = int(input("Please enter a two digit number:"))

first_digit = couple_number // 10 # divides the two-digit number entered by 10 returning it as a whole and decimal number.

second_digit = couple_number % 10 # extracts the decimal number.

digit_sum = first_digit + second_digit

print("The sum of the digits is:", digit_sum)

# Entering a Single-Digit Number To Find It Squared & Cubed:
single_number = int(input("Please enter a single number:"))

single_number_squared = math.sqrt(single_number)

single_number_cubed = math.cbrt(single_number)

print("The Number Squared is:", single_number_squared)

print("The Number Cubed is:", single_number_cubed)

# Entering A Number Of Inches To Find Its Inches As Yards & Feet:
inches = int(input("Please enter a number of inches:"))

yards = inches // 36

remaining_inches_from_yards = inches % 36

feet = remaining_inches_from_yards // 12 # feet

remaining_inches = remaining_inches_from_yards % 12

print(f"{inches} inches is equal to {yards} yards, {feet} feet, and {remaining_inches} inches.")

# Converting Minutes to Hours
total_minutes = int(input("Enter a number of minutes: "))

hours = total_minutes // 60

minutes = total_minutes % 60

print(f"{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")

# Converting Fahrenheit To Celsius
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")

# Figuring Out Birth Year
current_year = 2025
age = int(input("How old are you? "))

birth_year = current_year - age

print(f"You were born in approximately {birth_year}.")

# Area Of A Rectangle
rectangle_base = float(input("Enter the length for a rectangle: "))

rectangle_height = float(input("Enter the width for a rectangle: "))

rectangle_area = rectangle_base * rectangle_height

print(f"The area of the rectangle is {rectangle_area}.")

# Area Of A Triangle
triangle_base = float(input("Enter the length for a triangle: "))

triangle_height = float(input("Enter the width for a triangle: "))

triangle_area = (triangle_height * triangle_height) // 2

print(f"The area of the triangle is {triangle_area}.")

