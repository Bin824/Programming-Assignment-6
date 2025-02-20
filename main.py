"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""

import string

def find_longest_words(input_filename, output_filename):
    """
    This function reads each line of the input file and writes the longest word
    into the output file
    """
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            words = line.split()
            if words:
                longest_word = max(words, key=lambda word: len(word.strip(string.punctuation)))
                outfile.write(longest_word + '\n')

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    find_longest_words(input_file, output_file)
