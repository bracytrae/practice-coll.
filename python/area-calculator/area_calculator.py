# area-calculator

# simple area calculator for, triangle, rectangle, square and circle operations. 

import math

def area_calculator():

    area_calculator = True

    while area_calculator:

        print("==================\nArea Calculator 📐\n==================")

        print("\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")

        choice = input("\nChoose your option: ")

        while not choice.isdigit() or int(choice) not in [1,2,3,4,5]:

            print("\nInvalid choice. Please try again.")
            choice = input("\nChoose your option: ")

        choice = int(choice)  # safe to convert now
        print(f"\nWhich shape: {choice}")

        # Triangle
        if choice == 1:

            height = float(input("\nEnter the Height: "))
            base = float(input("Enter the Base: "))

            # - -

            area = (height * base) / 2
            print(f"Area of Triangle: {area}")

        # Rectangle
        elif choice == 2:

            length = float(input("\nEnter the Length: "))
            width = float(input("Enter the Width: "))

            # - -

            area = length * width
            print(f"Area of Rectangle: {area}")

        # Square
        if choice == 3:

            side = float(input("\nEnter the side: "))

            # - -

            area = math.pow(side, 2)
            print(f"Area of Square: {area}")

        # Circle
        elif choice == 4:

            radius = float(input("\nEnter the Radius: "))

            # - -

            area = math.pi * (radius ** 2)
            print(f"Area of Circle: {area}")

        # Quit
        elif choice == 5:

            area_calculator = False
            print("Thank you for using the area calculator!")

area_calculator()












