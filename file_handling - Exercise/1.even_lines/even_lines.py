symbol_for_replace = ["-", ",", ".", "!", "?"]
with open('./text.txt','r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = " ".join(line.strip().split()[::-1])
            for symbol in symbol_for_replace:
                result = result.replace(symbol, "@")
            print(result)