# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Gebriel Tessema
# 9/12/2026
# Change#:1
# Change(s) Made: Initial creation
# Date of Change: 9/12/2026
# Author: Gabriel Tessema
# Change Approved by: Catie Williams
# Date Moved to Production: 9/12/2026

# Welcome message
print("Welcome to my program")

# Retrieve company name
company_name = input("Enter your company name: ")

# Retrieve number of feet of fiber optic cable
feet_of_cable = float(input("Enter the number of feet of fiber optic cable: "))

# Calculate installation cost ($0.95 per foot)
total_cost = feet_of_cable * 0.95

# The receipt (formatted legibly)
#print("\n" + "=" * 35)
print("=" * 35)

print("          RECEIPT")
print("=" * 35)
print(f"Company Name: {company_name}")
print(f"Feet of Fiber Optic Cable: {feet_of_cable}")
print(f"Total Cost: ${total_cost:.2f}")
print("=" * 35)