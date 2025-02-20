"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""

def find_longest_word(line):
    """
    Finds and returns the longest word in a given line.
    If multiple words have the same length, the first occurring word is returned.
    """
    words = line.split()
    longest_word = max(words, key=len)
    return longest_word

def open_files(input_filename, output_filename):
    """
    Reads the input file line by line, finds the longest word in each line,
    and writes it to the output file.
    If the input file is not found, an error message is displayed.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as in_file:
            with open(output_filename, 'w', encoding='utf-8') as out_file:
                for line in in_file:
                    longest_word = find_longest_word(line)
                    if longest_word:
                        out_file.write(longest_word + '\n')
    except FileNotFoundError:
        print("Error: The input file was not found.")

def main():
    """
    Prompts the user for input and output file names
    """
    input_filename = input("Enter your input file name: ").strip()
    output_filename = input("Enter your output file name: ").strip()
    open_files(input_filename, output_filename)

if __name__ == "__main__":
    main()
