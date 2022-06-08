# Create a program that will receive commands until the command "End". The commands can be:
# •	"Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)
# •	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
# •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. 
# If the file does not exist, print: "An error occurred"
# •	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
    
# Input Commands:
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End



from os import remove
from os.path import exists

while True:
    line = input()
    if line == 'End':
        break

    command_parts = line.split("-")
    command, file_name = command_parts[0], command_parts[1]

    if command == 'Create':
        with open(f'./{file_name}', 'w') as file:
            pass

    elif command == "Add":
        content = command_parts[2]
        with open(f"./{file_name}", "a") as file:
            file.write(content + "\n")

    elif command == "Replace":
        if not exists(f"./{file_name}"):
            print("An error occurred")
            continue
        old_string, new_string = command_parts[2], command_parts[3]
        with open(f"./{file_name}", "r+") as file:
            file_content = file.read().replace(old_string, new_string)

            file.seek(0)
            file.truncate()
            file.write(file_content)

    else:
        if not exists(f"./{file_name}"):
            print("An error occurred")
            continue
        remove(f"./{file_name}")
