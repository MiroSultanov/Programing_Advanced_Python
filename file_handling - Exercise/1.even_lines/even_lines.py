# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you print the result, 
# replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

# Input text:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.


symbol_for_replace = ["-", ",", ".", "!", "?"]
with open('./text.txt','r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = " ".join(line.strip().split()[::-1])
            for symbol in symbol_for_replace:
                result = result.replace(symbol, "@")
            print(result)
