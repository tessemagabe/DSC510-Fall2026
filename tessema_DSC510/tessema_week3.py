"""
The professor comment:
                        The program has some logical errors and exception messages have some errors in grammar,
                        semantics, and spelling. Exceptions are not written to a log file or output to the Console.
                        Program looks good however your try block is too broad.
"""

# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Gebriel Tessema
# 09/21/2026
# Change#: 1
#Change(s) Made: 
# • try block now only wraps the input and the float conversion. The rest
#   of the calculation and printing is outside the try block.
# • Added a check to ensure the user does not enter a negative number or zero.
# • Fixed capitalization and spelling errors in the header and console messages.
# • Cleaned up the file by removing old commented-out code.
# Date of Change: 09/21/2026
# Author: Gebriel Tessema
# Change Approved by: Catie Williams
# Date Moved to Production: 09/22/2026

# -------------------------------
# Welcome message
# -------------------------------
print("\n" + "=" * 50)
print("   Welcome to the Fiber Optic Cable Cost Calculator")
print("=" * 50)

# -------------------------------
# Ask the user for the company name
# -------------------------------
company_name = input("Please enter your company name: ")

# -------------------------------
# Ask for the number of feet and calculate the cost.
# The try block catches non-numeric input.
# The else block runs if the input is a valid number.
# -------------------------------
try:
    size_of_optic_cable = float(
        input("Please enter the number of feet of cable to install: ")
    )
except ValueError:
    print("ERROR: Please enter a numeric value for the number of feet.")
else:
    # Check to make sure the user didn't enter zero or a negative number
    if size_of_optic_cable <= 0:
        print("ERROR: Please enter a positive number greater than zero.")
    else:
        # Price per foot based on how many feet are ordered
        cost_of_cable_under100 = 0.95      # up to and including 100 ft
        cost_of_cable_100_to_250 = 0.85    # more than 100 ft, up to 250 ft
        cost_of_cable_250_to_500 = 0.75    # more than 250 ft, up to 500 ft
        cost_of_cable_over500 = 0.55       # more than 500 ft

        # Decide which price per foot to use
        if size_of_optic_cable <= 100:
            cost_of_cable = size_of_optic_cable * cost_of_cable_under100
        elif size_of_optic_cable <= 250:
            cost_of_cable = size_of_optic_cable * cost_of_cable_100_to_250
        elif size_of_optic_cable <= 500:
            cost_of_cable = size_of_optic_cable * cost_of_cable_250_to_500
        else:
            cost_of_cable = size_of_optic_cable * cost_of_cable_over500

        # -------------------------------
        # Print the receipt
        # -------------------------------
        print("\n" + "+" * 25)
        print("        Receipt")
        print("+" * 25)
        print(f"Company name: {company_name}")
        print(f"Feet of cable: {size_of_optic_cable}")
        print(f"Total cost: ${cost_of_cable:.2f}")
