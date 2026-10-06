""" MY FINAL 5.1 program Assignment
Calculator and Average Program

This program performs basic mathematical operations
(addition, subtraction, multiplication, and division)
and calculates the average of numbers using two functions.

The program:
ask the user to enter the operation type
ask the user to enter the first number
ask the user to enter the second number
display the results of the calculation
ask user to enter numbers for average calculation
display the results of the average calculation
"""
#DSC 510
#Week 5
#Programming Assignment Week 5
#Author Gebriel Tessema
#10/02/2026
#Change Control Log:
#Change#:1
#Change(s) Made: Initial program with while loop menu,
#                 perform_calculation, and calculate_average.
#Change#:2
#Change(s) Made: Added input validation loops for zero-division
#                 and average count; wrapped division re-prompt
#                 in try/except. Removed trailing calculate_average()
#                 call after menu loop.
#Date of Change: 10/04/2026
#Author: Gebriel Tessema
#Change Approved by: Catie Williams
#Date Moved to Production: 10/05/2026

def perform_calculation(operation):

    try:
        first_number = float(input("Enter the first number you want to operate : "))
        second_number = float(input("Enter the second number you want to operate : "))
    except ValueError:
        print("Please enter numerical value only. Thank you")
        return None

    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        while second_number == 0:
            print("second number cannot be zero")
            try:
                second_number=float(input("Enter the second number you want to operate : "))
            except ValueError:
                print("Please enter numeric value only. Thank you")

    return first_number / second_number


def calculate_average():
    try:

        numbers_you_wish_to_input  = int(input("how many numbers you wish to average: "))

        while numbers_you_wish_to_input <= 0:
            print("Please enter numeric value greater than zero. Thank you.")

            numbers_you_wish_to_input = int(input("how many numbers you wish to average: "))

        num = 0

        for i in range(numbers_you_wish_to_input):

            numbers = float(input("Please, enter the numbers you wish to input : "))
            num = num + numbers

        print(f"The average is: {num/numbers_you_wish_to_input}")

    except ValueError:
        print("Invalid input: Please enter numeric value only, thank you")


def main():

    while True:

        operation = input("Enter the operation you want to perform "
                          " +, -, *, /, a for Average, s for stop : ")

        if operation.lower() in ["s", "stop"]:
            print("operation is stopped")
            break
        elif operation.lower() == "a":
            calculate_average()

        elif operation in ["+","-","*","/"]:
            outcome=perform_calculation(operation)

            if outcome is not None:
                print(outcome)
        else:
            print("Please enter a numeric value, thank you")


if __name__ == "__main__":
    main()
