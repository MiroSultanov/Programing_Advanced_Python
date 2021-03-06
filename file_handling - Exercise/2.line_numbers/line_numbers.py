# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and punctuation marks. 
# The result should be written to another text file. 

# Input text:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.


from string import punctuation

def count_symbol(line):
    punctuation_symbols = set(punctuation)
    letters_count = 0
    punctuations_count = 0

    for symbol in line:
        if symbol.isalpha():
            letters_count += 1
        elif symbol in punctuation_symbols:
            punctuations_count += 1
    return letters_count, punctuations_count

with open("./text.txt", "r") as input_file, open("./output.txt", "w") as output_file:
    for index, line in enumerate(input_file):
        letters, punctuations = count_symbol(line)
        output_file.write(f"Line {index + 1}: {line.strip()} ({letters})({punctuations})\n")
