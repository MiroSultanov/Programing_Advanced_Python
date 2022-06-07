# You are given a file called numbers.txt with the following content:
# 1
# 2
# 3
# 4
# 5

# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.


file_path = './text.txt' # File found
# file_path = './text2.txt'  # File not found

try:
    open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')
