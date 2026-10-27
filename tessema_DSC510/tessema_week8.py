# MY practice page
# 8.1 Programming Assignment that modified 7.1 assignment
"""
# Purpose:
             This program will modify our Gettysburg processing program from Week 7
             to generate a text file from the output rather than printing it to the screen
"""


#DSC 510
#Week 7
#Programming Assignment Week 8
#Author Gebriel Tessema
#10/21/2026
#Change#:1
#Change(s) Made: This program modify our Gettysburg processing program from Week 7
#                 to generate a text file from the output rather than printing it to the screen.
#                 The sorting function was also changed from a lambda function to a def function.
# Date of Change: 10/22/2026
#Author: Gebriel Tessema
#Change Approved by: Catie Williams
#Date Moved to Production: 10/27/2026

import string

"""Add each word to the dictionary. Parameters are the word and a dictionary"""
def add_word(word, frequency):
    if word:
        if word in frequency:
           frequency[word] += 1
        else:
            frequency[word] = 1

"""process the line: strip off various characters, split out the words, remove punctuation"""
def process_line(line, frequency):

    words = line.split()

    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        add_word(word, frequency)
# print(file_name)

"""This function use string formatting to print the output in a tabular format"""
# def pretty_print(word_counts):
#     print(f"{'Word':<20}{'Count':>5}")
#     print("-" * 25)
#
#     sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
#
#     for word, count in sorted_words:
#         print(f"{word:<20}{count:>5}")
"""This function performs the same operations as pretty_print from Week 7 and prints to a new file instead of to the screen."""
def process_file(frequency, filename):
    try:

        with open(filename, "a") as newfile:

            newfile.write(f"{'Word':<20}{'Count':>5}\n")
            newfile.write("-" * 25 + "\n")

        #where sorting function changed from a lambda function to a def function.
            def get_sort_key(pair):
                return -pair[1], pair[0]

            sorted_pair = sorted(frequency.items(), key=get_sort_key)

            for word, count in sorted_pair:
                newfile.write(f"{word:<20}{count:>5}\n")
    except FileNotFoundError:
        print("File not found")


def main():
    """The main method is the entry point to the program; open the file and call 'process_line' on each line"""
#     test_count = {}
#
# # proof that my add_word function works
#     add_word("python", test_count)
#     add_word("python", test_count)
#     add_word("java", test_count)
#
# # proof that my process_line function works
#     process_line("Python, Python! Java.", test_count)
#     process_file(test_count)
#     print(test_count)

    frequency = {}
    file_name = input("Please enter [gettysburg.txt] just for 8.1 assignment: ")
    new_file = input("Please enter the name of the file [frequency_report.txt]: ")

    if not new_file:
        new_file= "frequency_report.txt"

    try:

        with open(file_name, "r") as file:
            for line in file:
                process_line(line, frequency)

        with open(new_file, "w") as newfile:
            newfile.write(
                f"Length of the dictionary: {len(frequency)}\n\n"
            )

        process_file(frequency, new_file)

        print(f"please, find the written result at: {new_file}")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
        main()
