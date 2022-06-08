# Write a program that traverses a given directory for all files. Search through the first level of the directory only and write information about each found file 
# in report.txt. The files should be grouped by their extension. Extensions should be ordered by name alphabetically. The files with extensions should also be 
# sorted by name. report.txt should be saved in the chosen directory.

from os import listdir
from os.path import isdir, join


def directory_traversal(path, files_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), files_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


result = {}
directory_traversal('./', result)

for key, value in result.items():
    print(key, value)
