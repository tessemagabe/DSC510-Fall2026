# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Gebriel Tessema
# 09/21/2026
# Change#: 1
# Change(s) Made: Added if/elif/else pricing tiers and try/except
#                 error handling for user input.
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
# A try block is used in case the user types something
# that is not a number.
# -------------------------------
try:
    size_of_optic_cable = float(
        input("Please enter the number of feet of cable to install: ")
    )

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

# -------------------------------
# Handle bad input (non-numeric values)
# -------------------------------
except ValueError:
    print("Error: Please enter a numeric value for the number of feet.")