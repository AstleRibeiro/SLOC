import glob
import os

# take folder location as input
directory = input('Enter path: ')
print(directory)

os.chdir(directory)

# creating a dictionary to store the name and sloc of each class
names = {}

# assuming folder contains java code
for fn in glob.glob('*.java'):
    with open(fn) as f:
        names[fn] = sum(1 for line in f if line.strip() and not line.__contains__('//'))
        # finding the sloc excluding comments and whitespaces


# printing name and sloc of each class
for key, value in names.items():
    print(f'{key} : {value}')

# calculating the total sloc of the package
total = sum(names.values())

# printing sloc of the package
print(f'The total Source lines of code is : ' + str(total))