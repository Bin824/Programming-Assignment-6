"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""

def find_longest_words(input_filename, output_filename):
    """
    This function reads each line of the input file and writes the longest word
    into the output file. In case there are multiple longest words, the first one is written.
    """
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            words = line.split()
            if words:
                # Find the longest word in the line (the first one in case of ties)
                longest_word = max(words, key=len)
                outfile.write(longest_word + '\n')
            else:
                # If the line is empty, write an empty line
                outfile.write('\n')

if __name__ == "__main__":
    input_file = input("Enter your input file name: ")
    output_file = input("Enter your output file name: ")
    find_longest_words(input_file, output_file)
