"""
This program calculates the cost of fiber optic cable installation.

This program:
- Displays a welcome message
- Retrieve a company name
- Retrieve the cable length
- Display the cost per foot
- Calculates the total cost
- Displays a receipt
"""

#DSC 510
#Week 4
#Programming Assignment Week 4
#Author Gebriel Tessema
#09/29/2026
#Change Control Log:
#Change#:1
#Change(s) Made: Modify the If Statement program from Week 3
#Date of Change: 09/29/2026
#Author: Gebriel Tessema
#Change Approved by: Catie Williams
#Date Moved to Production:09/29/2026

FIBER_OPTIC_CABLE_NEEDED_UNDER_100 = 0.95
FIBER_OPTIC_CABLE_NEEDED_OVER_100 = 0.85
FIBER_OPTIC_CABLE_NEEDED_OVER_250 = 0.75
FIBER_OPTIC_CABLE_NEEDED_OVER_500 = 0.55


def display_message(message):
    """Displaying a welcome message"""
    return "$" * 60 + "\n" + message + "\n" +"$" * 60


def company_name():
    """ Retrieving the company name from the user"""
    return input("\n  Enter the company name, please: ")


def feet_fiber_optic_cable_needed():
    """Retrieving size in feet of fiber optic cable to be installed from the user"""

    #using try/except blocks to catch any ValueError exceptions
    try:
        size = float(input("  Enter the fiber optic cable needed in feet, please: "))

        if size <= 0:
            print("[ERROR] Please enter a positive number.")
            return feet_fiber_optic_cable_needed()
        return size

    except ValueError:
        print(" [[ERROR]] Please enter a numeric value")
        return feet_fiber_optic_cable_needed()

def price_per_foot_base(size):
    """Determines the cost per foot based on the cable length"""

    if size<=100:
        return FIBER_OPTIC_CABLE_NEEDED_UNDER_100
    elif size<=250:
        return FIBER_OPTIC_CABLE_NEEDED_OVER_100
    elif size<=500:
        return FIBER_OPTIC_CABLE_NEEDED_OVER_250
    else:
        return FIBER_OPTIC_CABLE_NEEDED_OVER_500


def calculate_cost(size, cost):
    """Evaluating total cost based upon the number of feet requested,"""
    return size * cost

def display_receipt(name, size, cost, total):
    """ Printing receipt to the user"""
    print("\n" + "=" * 50)
    print("                    RECEIPT")
    print("=" * 50)
    print(f"The size of the cable requested is = {size:.2f} feet")
    print(f"cost per foot = ${cost:.2f}")
    print(f"The name of the company is = {name}")
    print(f"Total cost = ${total:.2f}")


def main():
   """Main function that controls the program."""
   msg= display_message("\n    "+"welcome to my optic cable cost estimation program" + "\n    ")
   print(msg)
   name = company_name()
   size = feet_fiber_optic_cable_needed()
   cost = price_per_foot_base(size)
   total= calculate_cost(size, cost)
   display_receipt(name, size, cost, total)


if __name__ == "__main__":
    main()

