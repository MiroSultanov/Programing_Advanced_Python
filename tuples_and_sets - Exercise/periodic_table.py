number_of_elements = int(input())
chemical_compounds = set()

for _ in range(number_of_elements):
    current_element = set(input().split())
    chemical_compounds = chemical_compounds.union(current_element)

for el in chemical_compounds:
    print(el)