# Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print them, separating them with a single space. 
# The module should also be able to locate a specific number in the sequence. You can read more about the Fibonacci sequence here: 
# https://en.wikipedia.org/wiki/Fibonacci_number
# You will be receiving commands until the "Stop" command. The commands are:
# •	"Create Sequence {count}". Create a series of numbers up to a specific count and print them in the following format:
#            "{n1} {n2} … {n}"

# •	"Locate {number}"
# Check if the sequence contains the number. If it finds the number, it should print:
# "The number - {number} is at index {index}"
# And if it doesn't find it:
# "The number {number} is not in the sequence"


generated_sequence = []


def create_sequence(n):
    while generated_sequence:
        generated_sequence.pop()

    generated_sequence.append(0)
    generated_sequence.append(1)

    for _ in range(n - 2):
        generated_sequence.append(
            generated_sequence[-1] + generated_sequence[-2]
        )
    return generated_sequence


def locate(x):
    if x in generated_sequence:
        return generated_sequence.index(x)

    return None


