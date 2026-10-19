# MY practice page
# 7.1 Programming Assignment FINAL
"""
# Purpose:
             This program demonstrates the use of dictionaries by
             processing a text file and counting the occurrence of
             each word. Words are added to a dictionary and their
            frequencies are updated as they are encountered.
"""


#DSC 510
#Week 7
#Programming Assignment Week 7
#Author Gebriel Tessema
#10/17/2026
#Change#:1
#Change(s) Made: This program counts unique words in gettysburg.txt and prints them by frequency.
#Date of Change: 10/17/2026
#Author: Gebriel Tessema
#Change Approved by: Catie Williams
#Date Moved to Production: 10/20/2026

import string
import sys

"""Add each word to the dictionary. Parameters are the word and a dictionary"""
def add_word(word, word_counts):
    if word:
        if word in word_counts:
           word_counts[word] += 1
        else:
            word_counts[word] = 1

"""process the line: strip off various characters, split out the words, remove punctuation"""
def process_line(line, word_counts):

    words = line.split()

    for word in words:

        word = word.lower()
        word = word.strip(string.punctuation)

        add_word(word, word_counts)


"""This function use string formatting to print the output in a tabular format"""
def pretty_print(word_counts):
    print(f"{'Word':<20}{'Count':>5}")
    print("-" * 25)

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    for word, count in sorted_words:
        print(f"{word:<20}{count:>5}")



"""The main method is the entry point to the program; open the file and call 'process_line' on each line"""
def main():
    test_count = {}
# proof that my add_word function works
    add_word("python", test_count)
    add_word("python", test_count)
    add_word("java", test_count)

# proof that my process_line function works
    process_line("Python, Python! Java.", test_count)

    print(test_count)


    word_counts = {}

    try:
        with open("gettysburg.txt", "r") as file:

            for line in file:
                process_line(line, word_counts)

        print(f"Length of the dictionary: {len(word_counts)}")
        print()

        pretty_print(word_counts)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
        main()
