#My practice page Final
# 9.1 Programming Assignment
"""
Purpose:
    Demonstrate that you can interact with a web service
    to extract data in JSON and then parse the JSON response.
    Write a program that uses an open API to obtain data for
    the end user and interacting with a free API to make a GET request,
    retrieve JSON data, and Parse JSON data
"""
# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Gebriel Tessema
# 10/28/2026
# Change#:1
# Change(s) Made:Create a program which uses the Request library
# #           to make a GET request of the following API: Chuck Norris Jokes.
# Date of Change: 10/29/2026
# Author: Gebriel Tessema
# Change Approved by: Catie Williams
# Date Moved to Production: 11/02/2026

import requests

valid_categories = ["dev", "animal", "food", "movie"]

def main():

    print("-----------------------------------------------------------")
    print("\tWelcome to the Chuck Norris Joke Generator Program")
    print("-----------------------------------------------------------")

    while True:

        category = input("\nEnter a category (dev, animal, food, movie) [dev]: ").strip().lower()

        if not category:
            category = "dev"

        if category not in valid_categories:
            print("Invalid category. Please choose dev, animal, food, or movie.")
            continue

        url = f"https://api.chucknorris.io/jokes/random?category={category}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            print("\n----------------------------------------")
            print("Chuck Norris Joke")
            print("----------------------------------------")
            print(data["value"])

        except requests.exceptions.RequestException as error:
            print(f"An error occurred: {error}")

        while True:

            again = input(
                "\nWould you like another joke? (Y/N): "
            ).strip().upper()

            if again in ["Y", "N"]:
                break

            print("Invalid entry. Please enter Y or N.")

        if again == "N":
            break

    print("\nThank you for using the Chuck Norris Joke Generator!")


if __name__ == "__main__":
    main()