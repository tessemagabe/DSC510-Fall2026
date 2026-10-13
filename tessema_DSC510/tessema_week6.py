# FINAL
#6.1 Programming Assignment

"""
Weather Temperature pick up program

Author: Gebriel Tessema
Description:
    This script allow  the user to enter a series of temperatures in Celsius.
    It stores them in a list until a sentinel value (-333) is entered.
    Evaluate the temperatures and determine the largest and smallest temperature.
    It then print the largest and smallest temperatures in a legible format,
    and tells the user how many temperatures in the list.
"""
#DSC 510
#Week 6
#Programming Assignment Week 6
#Author Gebriel Tessema
#10/10/2026
#Change#:1
#Change(s) Made: Initial programming for a weather pickup program using strings and loops
#Date of Change: 10/10/2026
#Author: Gebriel Tessema
#Change Approved by: Catie Williams
#Date Moved to Production: 10/13/2026

def weather():
#An empty list called temperatures collect and print a summary report.
    temperatures = []

    print("\n ======\t\t[Type -333] to stop the program\t\t======")

    while True:
#Allowing the user to input a series of temperatures along with a sentinel value
        try:
            temp=float(input("please, enter your choice of temperature in Celsius :"))
        except ValueError:
            print("  !!!-> That is not a valid number. Please try again.")
            continue

        if temp == -333:
            break
        temperatures.append(temp)

#Evaluate the temperatures in the temperatures list to determine the largest and smallest temperature.
    if len(temperatures) > 0:
        largest = max(temperatures)
        smallest = min(temperatures)

        print("\n--- Temperatures Evaluation ---")

        for temp in temperatures:
            if temp < 0:
                print(f" {temp} Sorry, temperature freezing be careful!")
            elif temp < 10:
                print(f" {temp} Sorry, you’ll need a coat or sweater; it’s uncomfortable without warm clothing!")
            elif temp < 18:
                print(f"{temp} Temperature is  cool but not yet cold; a light jacket may be needed enjoy!")
            elif temp < 30:
                print(f"{temp} pleasant, comfortable for most people; like a sunny spring day be happy!")
            elif temp < 40:
                print(f" {temp} noticeably hot, often requiring light clothing and hydration")
            else:
                print(f" {temp} dangerous heat, as in heatwaves or desert climates")
        print("\n\t--- Summary ---")
        print(f"Largest temperature: {largest}°C")
        print(f"Smallest temperature: {smallest}°C")
        print(f"You entered \t{len(temperatures)} \ttemperatures.")

def main():
    print("+" * 55)
    print("\n\twelcome to my weather temperatures pick up program\n")
    print("+" * 55)

    weather()

    print("+" * 55)
    print("\n\tGood by, have a blessed one")
    print("+" * 55)




if __name__ == "__main__":
    main()

