# Calculates User Net Pay Given One's Tax Bracket.

first_name = input("Enter Your First Name:") # First Name.

last_name = input("Enter Your Last Name:") # Last Name.

full_name = first_name + " " + last_name # Full Name via concatenation.

monthly_gross_pay = float(input("Enter Your Monthly Gross Pay:")) # The only float, thus the only thing that we round using the format specifier ".2f" within conditions.

number_of_dependents = int(input("Enter Number Of Dependents:")) # Number of dependents.

if number_of_dependents <= 1: # 0 - 1

    tax_rate = .20 # 20%
    print(f"\n{full_name}")
    print(f"Monthly Gross Pay: {monthly_gross_pay:.2f}") # float, thus rounded.
    print(f"Number of Dependents: {number_of_dependents}")
    print(f"Tax Rate: % 20")
    net_pay = monthly_gross_pay - (monthly_gross_pay * tax_rate)
    print(f"Net Pay: {net_pay:.2f}") # float, thus rounded, net pay influenced by monthly gross pay.

elif number_of_dependents <= 3: # 2 - 3

    tax_rate = .15 # 15%
    print(f"\n{full_name}")
    print(f"Monthly Gross Pay: {monthly_gross_pay:.2f}") # float, thus rounded.
    print(f"Number of Dependents: {number_of_dependents}")
    print(f"Tax Rate: % 15")
    net_pay = monthly_gross_pay - (monthly_gross_pay * tax_rate)
    print(f"Net Pay: {net_pay:.2f}") # float, thus rounded, net pay influenced by monthly gross pay.

else: # 4+

    tax_rate = .10 # 10%
    print(f"\n{full_name}")
    print(f"Monthly Gross Pay: {monthly_gross_pay:.2f}") # float, thus rounded.
    print(f"Number of Dependents: {number_of_dependents}")
    print(f"Tax Rate: % 10")
    net_pay = monthly_gross_pay - (monthly_gross_pay * tax_rate)
    print(f"Net Pay: {net_pay:.2f}") # float, thus rounded, net pay influenced by monthly gross pay.

print("\nEnd Of Program, Thank You For Using My Net Pay Calculator")


