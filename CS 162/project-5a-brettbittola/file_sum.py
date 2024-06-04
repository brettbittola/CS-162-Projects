# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 10/21/2023
# Description: Reads a list of numbers taken from a text file and returns the sum.

def file_sum(text_file):
    """Reads a list of numbers in a text file and creates a new text file with the sum of those numbers"""
    try:
        with open(text_file, 'r') as infile:
            total = 0
            for line in infile:
                total += float(line.strip())
    except FileNotFoundError:
        print("The file was not found.")
        return

    with open('sum.txt', 'w') as outfile:
        outfile.write(str(total) + '\n')
